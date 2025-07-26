from langchain_community.vectorstores import PGVector
from .config import POSTGRES_URI
from .embedder import get_embedder

def store_documents(docs):
    embedder = get_embedder()
    store = PGVector.from_documents(
        documents=docs,
        embedding=embedder,
        collection_name="hsc_bangla_book",
        connection_string=POSTGRES_URI
    )
    return store
