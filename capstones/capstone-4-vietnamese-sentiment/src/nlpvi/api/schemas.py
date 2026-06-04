"""Pydantic v2 request/response models for the sentiment API."""

from __future__ import annotations

from pydantic import BaseModel, Field

from ..data import LABEL_NAMES


class SentimentRequest(BaseModel):
    texts: list[str] = Field(
        ...,
        min_length=1,
        max_length=256,
        description="Vietnamese review texts to classify",
        examples=[["Sản phẩm tuyệt vời, giao hàng nhanh", "Hàng kém chất lượng"]],
    )


class Scores(BaseModel):
    negative: float
    neutral: float
    positive: float


class Prediction(BaseModel):
    label: str = Field(..., description=f"one of {LABEL_NAMES}")
    scores: Scores


class SentimentResponse(BaseModel):
    predictions: list[Prediction]
    model_version: str | None = None


class HealthResponse(BaseModel):
    status: str
    version: str


class ReadyResponse(BaseModel):
    ready: bool
    model_loaded: bool
