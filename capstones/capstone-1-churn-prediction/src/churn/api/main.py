"""FastAPI app: /predict (single+batch), /health, /ready, /metrics."""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..predict import load_model, predict as run_predict
from ..train import train_core
from .schemas import (
    CustomerRecord,
    HealthResponse,
    PredictResponse,
    Prediction,
    PredictRequest,
    ReadyResponse,
)

logger = get_logger(__name__)

# Holds runtime state populated by the lifespan handler.
STATE: dict[str, object] = {"model": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the model on startup; train a tiny one if no artifact exists."""
    settings = get_settings()
    try:
        STATE["model"] = load_model(settings)
        logger.info("model loaded on startup")
    except FileNotFoundError:
        logger.warning("no artifact found; training a small fallback model")
        tiny = settings.model_copy(update={"synthetic_rows": 800})
        result = train_core(tiny, save=True)
        STATE["model"] = result.pipeline
        logger.info("fallback model trained", extra={"metrics": result.metrics})
    yield
    STATE["model"] = None


app = FastAPI(
    title="Churn Prediction API",
    version=__version__,
    description="Telco customer churn prediction service.",
    lifespan=lifespan,
)

Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)


@app.get("/health", response_model=HealthResponse, tags=["ops"])
def health() -> HealthResponse:
    return HealthResponse(version=__version__)


@app.get("/ready", response_model=ReadyResponse, tags=["ops"])
def ready() -> ReadyResponse:
    loaded = STATE.get("model") is not None
    return ReadyResponse(status="ready" if loaded else "not_ready", model_loaded=loaded)


@app.post("/predict", response_model=PredictResponse, tags=["inference"])
def predict_endpoint(payload: PredictRequest) -> PredictResponse:
    model = STATE.get("model")
    if model is None:
        raise HTTPException(status_code=503, detail="model not loaded")

    records = payload if isinstance(payload, list) else [payload]
    if not records:
        raise HTTPException(status_code=422, detail="empty request")

    dicts = [r.model_dump() if isinstance(r, CustomerRecord) else dict(r) for r in records]
    results = run_predict(dicts, model=model)
    preds = [Prediction(**r) for r in results]
    return PredictResponse(predictions=preds, count=len(preds))
