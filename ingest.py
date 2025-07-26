from rag_pipeline.pdf_loader import load_documents
from rag_pipeline.vectorstore import store_documents
from rag_pipeline.config import POSTGRES_URI

print("[DEBUG] Postgres URI:", POSTGRES_URI)

if __name__ == "__main__":
    print("[INFO] Loading PDF...")
    docs = load_documents("data/HSC26_Bangla1st_Paper.pdf")

    print(f"[INFO] Loaded {len(docs)} documents. Storing into vector DB...")
    store_documents(docs)

    print("[DONE] Ingestion complete.")

