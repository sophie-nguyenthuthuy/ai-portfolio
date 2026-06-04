"""Pydantic v2 request/response models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ClassifyResponse(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    probs: dict[str, float]
    backend: str


class OcrFields(BaseModel):
    total: float | None = None
    date: str | None = None
    invoice_no: str | None = None


class OcrResponse(BaseModel):
    engine: str
    text: str
    fields: OcrFields


class HealthResponse(BaseModel):
    status: str = "ok"
    app: str
    version: str


class ReadyResponse(BaseModel):
    ready: bool
    model_loaded: bool
    backend: str | None = None
    labels: list[str] = Field(default_factory=list)
