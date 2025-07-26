# Multilingual RAG System (English + বাংলা)

A **Retrieval-Augmented Generation (RAG)** system powered by **Gemini Pro**, supporting queries in both **English and Bangla**, grounded in knowledge extracted from the **HSC26 Bangla 1st Paper** PDF. The system retrieves relevant text chunks from a vector database and generates meaningful answers in natural language.

---

## Demo Queries

| Query                                           | Answer    |
| ----------------------------------------------- | --------- |
| অনুপমের বাবা কী করে জীবিকা নির্বাহ করতেন?                   | ওকালতি     |
| শম্ভুনাথ সেকরার হাতে কী পরখ করতে দিয়েছিলেন?                 |কল্যাণীর বিয়ের গহনা |
| Oporichita golper kothoker naam ki              |Anupam (অনুপম)|

---

## Features

* Supports queries in both English and Bangla
* Document-grounded answers using Gemini Pro
* Vector DB powered by PostgreSQL + `pgvector`
* LangChain-based modular architecture
* REST API with FastAPI
* Evaluation: Groundedness & Relevance

---

## System Workflow

Here’s how the RAG system works — step by step:

1. **Document Loading**:

   * The HSC26 Bangla 1st Paper PDF is loaded using `PyPDFLoader`, which breaks it into sentence-level chunks.
2. **Text Preprocessing & Chunking**:

   * Bangla/English sentences are auto-extracted and chunked semantically to preserve meaning.
3. **Embedding**:

   * Each chunk is transformed into a vector using Google's `embedding-001` model (Gemini's embedding model).
4. **Vector Storage**:

   * Vectors are stored in a PostgreSQL DB using the `pgvector` extension.
5. **Query Handling**:

   * User submits a Bangla or English query through the API.
6. **Retrieval**:

   * Top-k relevant chunks are retrieved via cosine similarity from the vector DB.
7. **Answer Generation**:

   * Gemini Pro receives the query + retrieved chunks and generates a grounded natural language answer.
8. **API Response**:

   * The system returns the final answer with reference sources (for transparency).

---

## Tools & Libraries Used

| Component        | Tech Stack                                    |
| ---------------- | --------------------------------------------- |
| LLM & Embeddings | Google Gemini Pro (via `google-generativeai`) |
| Vector DB        | PostgreSQL + `pgvector`                       |
| Framework        | LangChain                                     |
| API              | FastAPI                                       |
| PDF Loader       | LangChain's `PyPDFLoader`                     |
| Language Support | English & বাংলা (Bangla)                      |

---

## Setup Guide

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/multilingual-rag.git
cd multilingual-rag
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_api_key_here
POSTGRES_URI=postgresql://username:password@localhost:5432/ragdb
GVECTOR_CONNECTION_STRING=postgresql://username:password@localhost:5432/ragdb
```

Enable `pgvector` in PostgreSQL:

```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

### 4. Ingest the PDF into VectorDB

```bash
python ingest.py
```

### 5. Run the API Server

```bash
python run.py
```

---

## Sample Queries

Use cURL, Postman, or browser (if frontend added):

```bash
curl -X POST http://localhost:8000/query \
    -H "Content-Type: application/json" \
    -d '{"question": "শম্ভুনাথ সেকরার হাতে কী পরখ করতে দিয়েছিলেন?"}'
```

---

## API Documentation

### `POST /query`

**Request Body:**

```json
{
  "question": "শম্ভুনাথ সেকরার হাতে কী পরখ করতে দিয়েছিলেন?"
}
```

**Response:**

```json
{
  "answer": "কল্যাণীর বিয়ের গহনা",
  "sources": ["hsc26_bangla_1st_paper.pdf"]
}
```

---

## Evaluation Matrix

| Metric         | Description                                   | Result (Manual) |
| -------------- | --------------------------------------------- | --------------- |
| Groundedness   | Is the answer supported by retrieved context? |   Yes           |
| Relevance      | Are the top chunks semantically related?      |   Yes           |
| Language Match | Does it handle Bangla & English inputs?       |   Yes           |

---

## Design Decision FAQs

### What method did you use to extract the text?

* Used `PyPDFLoader` from LangChain.
* It supports Bangla and English and automatically creates sentence-level chunks for semantic precision.

### What chunking strategy did you choose?

* **Sentence-based chunking** from LangChain.
* Sentences are the best minimal semantically complete units — this helps in retrieving the most contextually relevant segments.

### What embedding model did you use?

* **Google Generative AI's `embedding-001` model**.
* Captures cross-lingual semantic meaning (ideal for Bangla + English) and integrates directly with Gemini/Gemini Pro.

### How are you comparing queries with stored chunks?

* Via **cosine similarity** using `pgvector`.
* It's efficient, widely supported, and highly effective for dense semantic embeddings.

### How do you ensure meaningful query-document comparison?

* Using semantically coherent chunks (sentence-level).
* The Gemini model receives both the user query and retrieved chunks for maximum context-aware answer generation.

### What if the query is vague?

* If the query lacks context, the system may still attempt to generate a response, but:

  * Retrieval quality drops
  * Gemini may “hallucinate” without grounding
  * Could be improved using: query rewriting, larger context window, hybrid (dense + keyword) search

### Are the results relevant?

* Yes, for tested queries.
* Further improvements could include:

  * Better chunk granularity (paragraph + sentence)
  * Hybrid retrieval (dense + sparse)
  * Expanding the document base

---

## File Structure

```
.
├── data/
│   └── hsc26_bangla_1st_paper.pdf
├── rag_pipeline/
│   ├── config.py
│   ├── pdf_loader.py
│   ├── embedder.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── rag_engine.py
│   └── api.py
├── ingest.py
├── run.py
├── requirements.txt
├── .env
├── .gitignore
├── venv
└── README.md

```
