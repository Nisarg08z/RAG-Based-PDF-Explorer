from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf_text(file) -> list[str]:
    reader = PdfReader(file)
    return [page.extract_text() or "" for page in reader.pages]

def split_text_to_chunks(pages: list[str], chunk_size: int, overlap: int) -> list:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    all_chunks = []
    for i, page in enumerate(pages):
        for j, chunk in enumerate(splitter.split_text(page)):
            all_chunks.append({
                "content": chunk,
                "metadata": {"page": i + 1, "chunk_id": f"p{i+1}_c{j+1}"}
            })
    return all_chunks
