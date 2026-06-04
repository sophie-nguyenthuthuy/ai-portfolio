"""Pydantic v2 request/response schemas for the churn API."""

from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, Field


class CustomerRecord(BaseModel):
    """A single customer's features for scoring."""

    tenure: int = Field(..., ge=0, description="Months as a customer")
    monthly_charges: float = Field(..., ge=0)
    total_charges: float = Field(..., ge=0)
    num_services: int = Field(..., ge=0)
    senior_citizen: int = Field(0, ge=0, le=1)
    contract: str = "month-to-month"
    payment_method: str = "electronic-check"
    internet_service: str = "fiber-optic"
    paperless_billing: str = "yes"
    gender: str = "female"

    model_config = {
        "json_schema_extra": {
            "example": {
                "tenure": 2,
                "monthly_charges": 95.0,
                "total_charges": 190.0,
                "num_services": 2,
                "senior_citizen": 1,
                "contract": "month-to-month",
                "payment_method": "electronic-check",
                "internet_service": "fiber-optic",
                "paperless_billing": "yes",
                "gender": "female",
            }
        }
    }


# Accept either a single record or a list of records on POST /predict.
PredictRequest = Union[CustomerRecord, list[CustomerRecord]]


class Prediction(BaseModel):
    churn_probability: float
    churn_label: int


class PredictResponse(BaseModel):
    predictions: list[Prediction]
    count: int


class HealthResponse(BaseModel):
    status: Literal["ok"] = "ok"
    version: str


class ReadyResponse(BaseModel):
    status: Literal["ready", "not_ready"]
    model_loaded: bool
