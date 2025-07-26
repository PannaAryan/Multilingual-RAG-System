from langchain_community.vectorstores import PGVector
from .config import POSTGRES_URI
from .embedder import get_embedder

def get_retriever():
    embedder = get_embedder()
    vectorstore = PGVector(
        collection_name="hsc_bangla_book",
        connection_string=POSTGRES_URI,
        embedding_function=embedder
    )
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 10})
