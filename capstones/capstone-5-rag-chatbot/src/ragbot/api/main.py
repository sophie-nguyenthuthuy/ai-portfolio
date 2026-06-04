"""FastAPI app: /chat, /ingest, /health, /ready, /metrics.

Lifespan builds the RAG pipeline (default offline components) and ingests the
bundled sample corpus so the container answers questions out of the box.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..pipeline import RAGPipeline
from .schemas import (
    ChatRequest,
    ChatResponse,
    HealthResponse,
    IngestRequest,
    IngestResponse,
    ReadyResponse,
)

logger = get_logger(__name__)

# Holds runtime state populated by the lifespan handler.
STATE: dict[str, object] = {"pipeline": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Build the pipeline and ingest the bundled sample corpus on startup."""
    settings = get_settings()
    pipeline = RAGPipeline(settings)
    n = pipeline.ingest_sample_corpus()
    STATE["pipeline"] = pipeline
    logger.info("pipeline ready", extra={"chunks": n})
    yield
    STATE["pipeline"] = None


app = FastAPI(
    title="RAG Chatbot API",
    version=__version__,
    description="Retrieval-augmented chatbot over internal SME documents.",
    lifespan=lifespan,
)

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


def _pipeline() -> RAGPipeline:
    pipeline = STATE.get("pipeline")
    if pipeline is None:
        raise HTTPException(status_code=503, detail="pipeline not ready")
    return pipeline  # type: ignore[return-value]


@app.get("/health", response_model=HealthResponse, tags=["ops"])
def health() -> HealthResponse:
    return HealthResponse(version=__version__)


@app.get("/ready", response_model=ReadyResponse, tags=["ops"])
def ready() -> ReadyResponse:
    pipeline = STATE.get("pipeline")
    indexed = pipeline.store.count() if pipeline is not None else 0  # type: ignore[union-attr]
    return ReadyResponse(status="ready" if indexed else "not_ready", chunks_indexed=indexed)


@app.post("/ingest", response_model=IngestResponse, tags=["ingestion"])
def ingest_endpoint(payload: IngestRequest) -> IngestResponse:
    pipeline = _pipeline()
    if not payload.paths and not payload.documents:
        raise HTTPException(status_code=422, detail="provide paths or documents")

    n = 0
    if payload.documents:
        n += pipeline.ingest_texts(payload.documents)
    if payload.paths:
        n += pipeline.ingest([Path(p) for p in payload.paths])
    return IngestResponse(ingested_chunks=n, total_chunks=pipeline.store.count())


@app.post("/chat", response_model=ChatResponse, tags=["chat"])
def chat_endpoint(payload: ChatRequest) -> ChatResponse:
    pipeline = _pipeline()
    result = pipeline.answer(payload.question, top_k=payload.top_k)
    return ChatResponse(**result)
