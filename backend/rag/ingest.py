from rag.loader import load_pdf
from rag.chunking import split_documents
from rag.vector_store import create_vector_store


def ingest(pdf_path):
    """
    Complete ingestion pipeline:
    PDF -> Documents -> Chunks -> ChromaDB
    """

    print("Loading PDF...")
    documents = load_pdf(pdf_path)

    print("Splitting Documents...")
    chunks = split_documents(documents)

    print("Creating Vector Database...")
    create_vector_store(chunks)

    print("Done!")