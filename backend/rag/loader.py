from langchain_community.document_loaders import PyPDFLoader


def load_pdf(pdf_path):
    """
    Loads a PDF file and returns all pages as Document objects.
    """

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents