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
    return {
        "answer": response["result"],
        "sources": [doc.metadata["source"] for doc in response["source_documents"]]
    }
