from document_loader import load_documents
from vector_store import create_vector_store
from llm import load_llm
from prompt import load_prompt


llm = load_llm()
prompt = load_prompt()


def initialize_assistant(folder_path):

    documents = load_documents(folder_path)

    retriever = create_vector_store(documents)

    return retriever


def ask_question(retriever, question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    sources = []

    for doc in docs:

        paper = doc.metadata.get("paper_name", "Unknown")

        page = doc.metadata.get("page", "Unknown")

        sources.append(f"{paper} (Page {page + 1})")

    final_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(final_prompt)

    return response.content, list(set(sources))