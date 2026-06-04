"""FastAPI app exposing classify + ocr + health/ready/metrics endpoints.

On startup the lifespan handler loads the latest saved model, or trains a tiny
one on synthetic images if none exists, so the container is self-sufficient.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, File, HTTPException, UploadFile
from prometheus_fastapi_instrumentator import Instrumentator

from .. import __version__
from ..config import get_settings
from ..logging_conf import get_logger
from ..predict import classify as run_classify
from ..predict import load_model
from ..predict import ocr as run_ocr
from .schemas import (
    ClassifyResponse,
    HealthResponse,
    OcrFields,
    OcrResponse,
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
        log.info("model ready: backend=%s", metadata.get("backend", "unknown"))
    except Exception as exc:  # pragma: no cover - defensive
        log.error("failed to load/train model on startup: %s", exc)
        STATE["model"] = None
    yield
    STATE.clear()


async def _read_upload(file: UploadFile, max_bytes: int) -> bytes:
    data = await file.read()
    if not data:
        raise HTTPException(status_code=400, detail="empty file upload")
    if len(data) > max_bytes:
        raise HTTPException(status_code=413, detail="file too large")
    return data


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        description="Document image classification + invoice OCR service.",
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
        meta = STATE.get("metadata", {})
        return ReadyResponse(
            ready=loaded,
            model_loaded=loaded,
            backend=meta.get("backend"),
            labels=meta.get("label_names", []),
        )

    @app.post("/classify", response_model=ClassifyResponse, tags=["vision"])
    async def classify(file: UploadFile = File(...)) -> ClassifyResponse:
        model = STATE.get("model")
        if model is None:
            raise HTTPException(status_code=503, detail="model not loaded")
        data = await _read_upload(file, settings.max_upload_bytes)
        try:
            out = run_classify(
                data, settings=settings, model=model, metadata=STATE.get("metadata", {})
            )
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"invalid image: {exc}") from exc
        return ClassifyResponse(**out)

    @app.post("/ocr", response_model=OcrResponse, tags=["vision"])
    async def ocr(file: UploadFile = File(...)) -> OcrResponse:
        data = await _read_upload(file, settings.max_upload_bytes)
        try:
            out = run_ocr(data, settings=settings)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f"invalid image: {exc}") from exc
        return OcrResponse(
            engine=out["engine"],
            text=out["text"],
            fields=OcrFields(**out["fields"]),
        )

    return app


app = create_app()
