import os
import time
from datetime import datetime

import streamlit as st
from PyPDF2 import PdfReader

from pdf_utils import load_pdf_text, split_text_to_chunks
from vector_utils import create_vector_store
from qa_engine import answer_question

st.set_page_config(page_title="RAG-Based PDF Explorer", layout="wide")

# --- styles ---
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Settings")
    openai_key = st.text_input("OpenAI API Key", type="password")
    chunk_size = st.slider("Chunk Size", 500, 2000, 1000)
    chunk_overlap = st.slider("Chunk Overlap", 0, 500, 200)
    num_results = st.slider("Top K Results", 1, 10, 5)

    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
        st.success("API Key Set")
    else:
        st.warning("Please enter your OpenAI API Key")

# --- Session State ---
for key, default in {
    'collection': None,
    'pdf_stats': {},
    'vector_store': None,
    'pdf_loaded': False,
    'query_history': [],
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

# --- File Upload & Processing ---
st.title("📄 RAG-Based PDF Explorer - Ask Questions to Your PDF")
uploaded = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded:
    new_hash = hash(uploaded.getvalue())
    if st.session_state.pdf_stats.get('hash') != new_hash:
        st.session_state.pdf_loaded = False

    if not st.session_state.pdf_loaded and openai_key:
        with st.spinner("Processing PDF..."):
            # Extract
            pages = load_pdf_text(uploaded)
            full_text = "\n".join(pages)

            # Chunk
            chunks = split_text_to_chunks(pages, chunk_size, chunk_overlap)

            # Embed
            collection_name = f"collection_{int(time.time())}"
            vector_store = create_vector_store(chunks, collection_name)

            # Save state
            st.session_state.vector_store = vector_store
            st.session_state.collection = collection_name
            st.session_state.pdf_stats = {
                "pages": len(pages),
                "chunks": len(chunks),
                "filename": uploaded.name,
                "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "hash": new_hash
            }
            st.session_state.pdf_loaded = True
            st.rerun()

# --- Stats ---
if st.session_state.pdf_loaded:
    stats = st.session_state.pdf_stats
    st.success(f"📄 {stats['filename']} | 📑 {stats['pages']} pages | 🔹 {stats['chunks']} chunks")
    st.caption(f"Processed at: {stats['processed_at']} | Collection: {st.session_state.collection}")

# --- Q&A ---
if st.session_state.vector_store:
    question = st.text_input("Ask a question about the PDF...")
    if st.button("Get Answer") and question:
        with st.spinner("Generating answer..."):
            response, sources = answer_question(
                question,
                st.session_state.vector_store,
                openai_key,
                num_results
            )

            st.markdown("### 🤖 Answer")
            st.info(response)

            st.markdown("### 📚 Sources")
            for i, src in enumerate(sources):
                with st.expander(f"Source {i+1} - Page {src['page']}"):
                    st.write(src["content"])

            st.session_state.query_history.append((question, response))
