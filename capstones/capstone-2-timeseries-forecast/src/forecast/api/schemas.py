"""Pydantic v2 request/response models."""

from __future__ import annotations

from pydantic import BaseModel, Field


class ForecastRequest(BaseModel):
    horizon: int = Field(default=14, ge=1, le=365, description="steps ahead to forecast")


class ForecastPoint(BaseModel):
    date: str
    yhat: float
    yhat_lower: float
    yhat_upper: float


class ForecastResponse(BaseModel):
    model_name: str
    horizon: int
    points: list[ForecastPoint]


class HealthResponse(BaseModel):
    status: str = "ok"
    app: str
    version: str


class ReadyResponse(BaseModel):
    ready: bool
    model_loaded: bool
    model_name: str | None = None
