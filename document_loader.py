import os
from langchain_community.document_loaders import PyPDFLoader


def load_documents(path):

    documents = []

    # Single PDF
    if os.path.isfile(path):

        loader = PyPDFLoader(path)

        docs = loader.load()

        file_name = os.path.basename(path)

        for doc in docs:
            doc.metadata["paper_name"] = file_name

        documents.extend(docs)

    # Folder containing PDFs
    elif os.path.isdir(path):

        for file in os.listdir(path):

            if file.endswith(".pdf"):

                file_path = os.path.join(path, file)

                loader = PyPDFLoader(file_path)

                docs = loader.load()

                for doc in docs:
                    doc.metadata["paper_name"] = file

                documents.extend(docs)

    else:
        raise ValueError("Invalid file or folder path.")

    return documents