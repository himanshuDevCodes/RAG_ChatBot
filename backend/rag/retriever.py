from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
import os
from config import CHROMA_DB
from rag.embeddings import get_embedding_model

def vector_store_exists():
    """
    Check whether the vector database exists.

    Returns:
        bool: True if ChromaDB exists, otherwise False.
    """

    return os.path.exists(CHROMA_DB)

def get_vector_store():
    """
    Load the existing Chroma database.
    """

    embeddings = get_embedding_model()

    vector_db = Chroma(
        persist_directory=CHROMA_DB,
        embedding_function=embeddings
    )

    return vector_db


def retrieve_context(question, k=3):
    """
    Retrieve the most relevant chunks for a question.
    """

    vector_db = get_vector_store()

    docs = vector_db.similarity_search(
        question,
        k=k
    )

      # Convert Document objects into one text string
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    return context