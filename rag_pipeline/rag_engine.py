# rag_engine.py

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA
from .retriever import get_retriever
from .config import GOOGLE_API_KEY


def get_rag_chain():
    """
    Builds a Retrieval-Augmented Generation (RAG) QA chain using:
    - Google Gemini-Pro LLM
    - PostgreSQL-backed vector retriever

    Returns:
        RetrievalQA chain that can be used to ask questions and get answers from documents.
    """
    # Load the retriever from vector DB
    retriever = get_retriever()

    # Set up Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        google_api_key=GOOGLE_API_KEY,
        convert_system_message_to_human=True  
    )

    # Construct RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",                # Use "stuff" chain type for simple input formatting
        retriever=retriever,
        return_source_documents=True       # Return source docs with the answer
    )

    return qa_chain
