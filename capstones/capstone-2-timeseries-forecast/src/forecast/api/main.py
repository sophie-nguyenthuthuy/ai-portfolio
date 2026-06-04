"""FastAPI app exposing forecasting + health/ready/metrics endpoints.

On startup the lifespan handler loads the latest saved model, or fits a baseline
on synthetic-or-real data if none exists, so the container is self-sufficient.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..predict import forecast as run_forecast
from ..predict import load_model
from .schemas import (
    ForecastPoint,
    ForecastRequest,
    ForecastResponse,
    HealthResponse,
    ReadyResponse,
)

log = get_logger(__name__)

# Module-level state populated by the lifespan handler.
STATE: dict[str, Any] = {"model": None, "metadata": {}}


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    try:
        model, metadata = load_model(settings)
        STATE["model"] = model
        STATE["metadata"] = metadata
        log.info("model ready: %s", metadata.get("model_name", "unknown"))
    except Exception as exc:  # pragma: no cover - defensive
        log.error("failed to load/train model on startup: %s", exc)
        STATE["model"] = None
    yield
    STATE.clear()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        description="Vietnam retail-sales / stock close time-series forecasting.",
        lifespan=lifespan,
    )
    Instrumentator().instrument(app).expose(app, endpoint="/metrics", include_in_schema=False)

    @app.get("/health", response_model=HealthResponse, tags=["ops"])
    def health() -> HealthResponse:
        return HealthResponse(status="ok", app=settings.app_name, version=__version__)

    @app.get("/ready", response_model=ReadyResponse, tags=["ops"])
    def ready() -> ReadyResponse:
        model = STATE.get("model")
        loaded = model is not None
        return ReadyResponse(
            ready=loaded,
            model_loaded=loaded,
            model_name=STATE.get("metadata", {}).get("model_name"),
        )

    @app.post("/forecast", response_model=ForecastResponse, tags=["forecast"])
    def forecast(req: ForecastRequest) -> ForecastResponse:
        model = STATE.get("model")
        if model is None:
            raise HTTPException(status_code=503, detail="model not loaded")
        points = run_forecast(req.horizon, settings=settings, model=model)
        return ForecastResponse(
            model_name=STATE.get("metadata", {}).get("model_name", getattr(model, "name", "unknown")),
            horizon=req.horizon,
            points=[ForecastPoint(**p) for p in points],
        )

    return app


app = create_app()
