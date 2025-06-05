from langchain.vectorstores import Qdrant
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document

QDRANT_URL = "http://44.222.24.96:6333"

def create_vector_store(chunks, collection_name):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    docs = [Document(page_content=ch["content"], metadata=ch["metadata"]) for ch in chunks]
    return Qdrant.from_documents(docs, embeddings, collection_name=collection_name, url=QDRANT_URL)
