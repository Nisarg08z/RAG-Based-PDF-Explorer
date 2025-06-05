from langchain.chat_models import ChatOpenAI

def answer_question(question, vector_store, api_key, k):
    matches = vector_store.similarity_search(question, k=k)
    context = "\n\n".join(
        f"[Page {m.metadata.get('page')}] {m.page_content}" for m in matches
    )
    prompt = f"""
You are a helpful assistant answering based on the following PDF excerpts:

{context}

User question: {question}

Respond clearly, professionally, and always mention the page numbers.
"""
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.1, openai_api_key=api_key)
    answer = llm.predict(prompt)

    return answer, [{"page": m.metadata.get("page"), "content": m.page_content} for m in matches]
