import os

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def create_vector_store(documents):

    persist_directory = "./chroma_db"

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load existing vector database
    if os.path.exists(persist_directory):

        print("\nLoading existing ChromaDB...\n")

        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )

    # Otherwise create it
    else:

        print("\nCreating ChromaDB...\n")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_documents(documents)

        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=persist_directory
        )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 4}
    )

    return retriever