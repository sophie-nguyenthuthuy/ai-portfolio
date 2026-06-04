"""FastAPI app: POST /run (research a question), plus /health, /ready, /metrics.

The lifespan handler builds the agent graph and tool registry once at startup so
each request reuses them. Defaults to the offline FakeLLM + SimpleGraph backends.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..graph import build_graph
from ..logging_conf import get_logger
from ..pipeline import run as run_agent
from .schemas import HealthResponse, ReadyResponse, RunRequest, RunResponse

logger = get_logger(__name__)

# Holds runtime state populated by the lifespan handler.
STATE: dict[str, object] = {"graph": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Build the agent graph (LLM + tool registry) on startup."""
    settings = get_settings()
    STATE["graph"] = build_graph(settings)
    logger.info(
        "agent graph built",
        extra={"backend": getattr(STATE["graph"], "backend", "unknown")},
    )
    yield
    STATE["graph"] = None


app = FastAPI(
    title="Research Agent API",
    version=__version__,
    description="A LangGraph-style research agent: plan -> tools -> cited answer.",
    lifespan=lifespan,
)

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


@app.get("/health", response_model=HealthResponse, tags=["ops"])
def health() -> HealthResponse:
    return HealthResponse(version=__version__)


@app.get("/ready", response_model=ReadyResponse, tags=["ops"])
def ready() -> ReadyResponse:
    loaded = STATE.get("graph") is not None
    return ReadyResponse(status="ready" if loaded else "not_ready", graph_loaded=loaded)


@app.post("/run", response_model=RunResponse, tags=["agent"])
def run_endpoint(payload: RunRequest) -> RunResponse:
    graph = STATE.get("graph")
    if graph is None:
        raise HTTPException(status_code=503, detail="agent graph not loaded")

    settings = get_settings()
    if payload.max_steps is not None:
        settings = settings.model_copy(update={"max_steps": payload.max_steps})

    try:
        result = run_agent(payload.question, settings=settings, graph=graph)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return RunResponse(**result)
