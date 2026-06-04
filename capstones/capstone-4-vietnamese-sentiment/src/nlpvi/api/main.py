"""FastAPI application exposing sentiment prediction plus ops endpoints."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..predict import load_model, predict, reset_cache
from .schemas import (
    HealthResponse,
    Prediction,
    ReadyResponse,
    SentimentRequest,
    SentimentResponse,
)

log = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load (or train) the model on startup so the container is self-sufficient."""
    settings = get_settings()
    try:
        load_model(settings, train_if_missing=True)
        app.state.model_ready = True
        log.info("startup: model ready")
    except Exception as exc:  # pragma: no cover - defensive
        app.state.model_ready = False
        log.warning("startup: model not ready: %s", exc)
    yield
    reset_cache()


def create_app() -> FastAPI:
    app = FastAPI(
        title="nlpvi — Vietnamese Sentiment API",
        version=__version__,
        lifespan=lifespan,
    )
    app.state.model_ready = False
    Instrumentator().instrument(app).expose(app, endpoint="/metrics")

    @app.get("/health", response_model=HealthResponse, tags=["ops"])
    def health() -> HealthResponse:
        return HealthResponse(status="ok", version=__version__)

    @app.get("/ready", response_model=ReadyResponse, tags=["ops"])
    def ready() -> ReadyResponse:
        loaded = bool(getattr(app.state, "model_ready", False))
        return ReadyResponse(ready=loaded, model_loaded=loaded)

    @app.post("/sentiment", response_model=SentimentResponse, tags=["inference"])
    def sentiment(req: SentimentRequest) -> SentimentResponse:
        try:
            raw = predict(req.texts)
        except Exception as exc:  # pragma: no cover - defensive
            raise HTTPException(status_code=500, detail=str(exc)) from exc
        from ..predict import _STATE

        return SentimentResponse(
            predictions=[Prediction(**r) for r in raw],
            model_version=(_STATE.get("metadata") or {}).get("model_version"),
        )

    return app


app = create_app()
