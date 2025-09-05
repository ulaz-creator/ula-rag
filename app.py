from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os

API_TOKEN = os.getenv("RAG_API_TOKEN", "")

app = FastAPI(title="Ula RAG API")

class QueryIn(BaseModel):
    query: str
    top_k: int | None = 5
    filters: dict | None = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query_rag(payload: QueryIn, authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing Bearer token")
    token = authorization.split(" ", 1)[1]
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    # TODO: tutaj Twój retriever/generator
    return {
        "answer": "Przykładowa odpowiedź z Twojego RAG 🚀",
        "sources": [
            {"id": "doc1", "title": "Test źródło", "url": None, "score": 0.9, "chunk": "Fragment przykładowy"}
        ]
    }
