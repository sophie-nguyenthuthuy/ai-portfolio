"""FastAPI serving app.

Loads the current **Production** model from the configured registry on startup.
If the registry is empty, runs the reference flow once to self-bootstrap so the
container is self-sufficient. Exposes /predict, /health, /ready, /metrics,
/model/info and POST /reload.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..predict import predict as run_predict
from .schemas import (
    CustomerRecord,
    HealthResponse,
    ModelInfoResponse,
    Prediction,
    PredictRequest,
    PredictResponse,
    ReadyResponse,
    ReloadResponse,
)

logger = get_logger(__name__)

# Runtime state populated by the lifespan handler / reload.
STATE: dict[str, object] = {"model": None, "version": None, "stage": None, "metrics": {}}


def _load_from_registry() -> bool:
    """Load the current Production model into STATE. Returns True on success."""
    from ..registry import PRODUCTION, RegistryError, get_registry

    settings = get_settings()
    reg = get_registry(settings)
    try:
        mv = reg.current(PRODUCTION)
        if mv is None:
            return False
        STATE["model"] = reg.load_model(stage=PRODUCTION)
        STATE["version"] = mv.version
        STATE["stage"] = mv.stage
        STATE["metrics"] = mv.metrics
        logger.info("loaded production model", extra={"version": mv.version})
        return True
    except RegistryError:
        return False


def _bootstrap() -> None:
    """Run the reference flow once so a fresh deployment has a Production model."""
    from ..pipeline import run_flow

    logger.warning("no Production model found; bootstrapping via reference flow")
    settings = get_settings().model_copy(update={"synthetic_rows": 1200})
    run_flow(settings)
    _load_from_registry()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Honour a pre-populated model (e.g. injected by tests); else load/bootstrap.
    if STATE.get("model") is None:
        if not _load_from_registry():
            _bootstrap()
    yield
    STATE.update({"model": None, "version": None, "stage": None, "metrics": {}})


app = FastAPI(
    title="MLOps Platform API",
    version=__version__,
    description="Serves the current Production model from the registry.",
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


@app.get("/model/info", response_model=ModelInfoResponse, tags=["ops"])
def model_info() -> ModelInfoResponse:
    settings = get_settings()
    return ModelInfoResponse(
        model_name=settings.model_name,
        version=STATE.get("version"),
        stage=STATE.get("stage"),
        metrics=STATE.get("metrics") or {},
        loaded=STATE.get("model") is not None,
    )


@app.post("/reload", response_model=ReloadResponse, tags=["ops"])
def reload_model() -> ReloadResponse:
    """Reload the current Production model from the registry (after a promotion)."""
    ok = _load_from_registry()
    if not ok:
        raise HTTPException(status_code=503, detail="no Production model available")
    return ReloadResponse(reloaded=True, version=STATE.get("version"), stage=STATE.get("stage"))


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
