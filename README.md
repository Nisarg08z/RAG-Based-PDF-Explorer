"# RAG-Based-PDF-Explorer" 
---

# 📄 RAG-Based PDF Explorer

A **RAG (Retrieval-Augmented Generation)** powered Streamlit app that allows you to **ask questions from uploaded PDF files** using **LangChain**, **OpenAI**, and **Qdrant** for document retrieval and answer generation.

---

## 🔍 Features

* 🧠 Semantic search using vector embeddings (OpenAI Embeddings + Qdrant)
* 📄 PDF parsing and chunking with LangChain
* 💬 Natural language Q\&A using OpenAI GPT-4.1-mini
* 📊 Streamlit interface with styled results
* 🛠 Customizable chunk size, overlap, and number of results
* 🔐 API key input with secure session state
* 📚 Source page and content shown for transparency

---

## 🧱 Tech Stack

* **Frontend/UI**: Streamlit + Custom CSS
* **PDF Parsing**: PyPDF2
* **Text Chunking**: LangChain's `RecursiveCharacterTextSplitter`
* **Embeddings**: OpenAI `text-embedding-3-small`
* **Vector Store**: Qdrant (via Docker)
* **Language Model**: OpenAI GPT-4.1-mini (LangChain wrapper)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pdf-rag-explorer.git
cd pdf-rag-explorer
```

### 2. Install Dependencies

We recommend using a virtual environment:

```bash
pip install -r requirements.txt
```

> Make sure you have Python 3.8 or higher.

### 3. Start Qdrant via Docker

Ensure you have Docker installed. Then run:

```bash
docker-compose up -d
```

This will start the Qdrant vector database on port `6333`.

### 4. Run the App

```bash
streamlit run app.py
```

Open in your browser at `http://localhost:8501`

---

## 🔑 OpenAI API Key

You will need an OpenAI API key to generate answers. Enter your key in the sidebar of the app.

---

## 🗂 Project Structure

```
├── app.py                  # Streamlit UI and main logic
├── pdf_utils.py            # PDF loading and text chunking
├── vector_utils.py         # Qdrant vector store creation
├── qa_engine.py            # Answer generation using GPT-4.1-mini
├── styles.css              # UI styles for Streamlit
├── docker-compose.yml      # Qdrant vector database setup
└── README.md               # You're here!
```

---

## 📸 Demo

![Screenshot (209)](https://github.com/user-attachments/assets/eb3c6b41-8955-4580-a0d5-f2003bf71df1)

---

## 📝 Example Workflow

1. Upload a PDF file.
2. The app will extract and chunk text using LangChain.
3. Chunks are embedded and stored in Qdrant.
4. Ask questions using natural language.
5. The app uses GPT-4.1-mini with relevant context to generate an answer.
6. Sources are shown with page numbers and matched content.

---

## 🧪 Requirements

```
streamlit
PyPDF2
openai
langchain
qdrant-client
python-dotenv
```

You can create a `requirements.txt` with:

```bash
pip freeze > requirements.txt
```

---

## 📦 Deployment

* Local: Just run Streamlit and Docker.
* Cloud: Deploy to platforms like Streamlit Community Cloud, Azure, or Hugging Face Spaces (ensure Qdrant is available as a service or use Qdrant Cloud).

---

## 📚 Credits

* [LangChain](https://github.com/langchain-ai/langchain)
* [Qdrant](https://qdrant.tech/)
* [OpenAI](https://openai.com/)
* [Streamlit](https://streamlit.io/)

---

## 📜 License

MIT License. See [LICENSE](LICENSE) for details.

---


