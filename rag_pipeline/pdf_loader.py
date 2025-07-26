from langchain_community.document_loaders import PyPDFLoader

def load_documents(pdf_path):
    loader = PyPDFLoader(pdf_path)
    return loader.load()
