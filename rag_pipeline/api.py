from fastapi import FastAPI, Request
from pydantic import BaseModel
from .rag_engine import get_rag_chain

app = FastAPI()
qa = get_rag_chain()

class Query(BaseModel):
    question: str

@app.post("/query")
def query_rag(q: Query):
    response = qa.invoke(q.question)
    sources = list(set([doc.metadata.get("source", "unknown") for doc in response["source_documents"]]))
    return {
        "answer": response["result"],
        "sources": sources
    }

