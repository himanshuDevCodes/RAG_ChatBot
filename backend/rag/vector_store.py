from langchain_community.vectorstores import Chroma
import os
import shutil
from config import CHROMA_DB
from rag.embeddings import get_embedding_model


def create_vector_store(chunks):
    """
    Create a new Chroma vector database.

    If an old database exists, delete it first so that
    only the latest uploaded PDF is searchable.
    """
    # Delete previous vector database
    if os.path.exists(CHROMA_DB):
        shutil.rmtree(CHROMA_DB)

    # Create vector database from document chunks
    embeddings = get_embedding_model()

    vector_db = Chroma.from_documents(
        documents=chunks,                 #document chunk
        embedding=embeddings,             #Emedding model
        persist_directory=CHROMA_DB       #Folder for store vectors
    )

    return vector_db