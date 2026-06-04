"""Pydantic v2 request/response schemas for the RAG chatbot API."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """A user question; optional top_k override for retrieval."""

    question: str = Field(..., min_length=1, description="User question")
    top_k: int | None = Field(None, ge=1, le=20, description="Override retrieval depth")

    model_config = {
        "json_schema_extra": {
            "example": {"question": "Nhan vien duoc bao nhieu ngay nghi phep?", "top_k": 4}
        }
    }


class Source(BaseModel):
    rank: int
    source: str
    chunk_index: int
    score: float
    text: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[Source]
    question: str


class IngestRequest(BaseModel):
    """Ingest either filesystem paths or inline documents (name -> text)."""

    paths: list[str] | None = Field(None, description="Files or directories to ingest")
    documents: dict[str, str] | None = Field(
        None, description="Inline docs as a mapping of name -> text"
    )

    model_config = {
        "json_schema_extra": {
            "example": {"documents": {"faq.md": "Gio lam viec la tu 9h den 18h."}}
        }
    }


class IngestResponse(BaseModel):
    ingested_chunks: int
    total_chunks: int


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    version: str


class ReadyResponse(BaseModel):
    status: Literal["ready", "not_ready"]
    chunks_indexed: int
