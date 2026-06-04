"""Train -> predict on synthetic data; assert shapes, scores, persistence."""

from __future__ import annotations

import json
from pathlib import Path

import joblib

from churn.predict import load_model, predict
from churn.train import train_core


def test_train_scores_above_chance(trained):
    assert trained.metrics["roc_auc"] > 0.7  # clear learnable signal
    assert trained.metrics["pr_auc"] > 0.3
    assert 0.0 <= trained.metrics["accuracy"] <= 1.0
    assert trained.metrics["n_test"] > 0


def test_artifact_and_metadata_persisted(trained, settings):
    assert Path(trained.model_path).exists()
    meta = json.loads(Path(trained.metadata_path).read_text())
    assert "metrics" in meta and "params" in meta
    assert meta["params"]["classifier"] == "logistic_regression"


def test_load_model_roundtrip(trained, settings):
    model = load_model(settings)
    record = {
        "tenure": 1,
        "monthly_charges": 100.0,
        "total_charges": 100.0,
        "num_services": 2,
        "senior_citizen": 1,
        "contract": "month-to-month",
        "payment_method": "electronic-check",
        "internet_service": "fiber-optic",
        "paperless_billing": "yes",
        "gender": "male",
    }
    out = predict([record], model=model)
    assert len(out) == 1
    assert 0.0 <= out[0]["churn_probability"] <= 1.0
    assert out[0]["churn_label"] in (0, 1)


def test_predict_batch_and_missing_columns(trained):
    records = [
        {"tenure": 60, "monthly_charges": 30.0, "total_charges": 1800.0, "num_services": 1,
         "contract": "two-year", "internet_service": "none"},  # missing several cols
        {"tenure": 1, "monthly_charges": 110.0, "total_charges": 110.0, "num_services": 5,
         "contract": "month-to-month", "internet_service": "fiber-optic", "senior_citizen": 1},
    ]
    out = predict(records, model=trained.pipeline)
    assert len(out) == 2
    # Loyal two-year customer should be less likely to churn than the new one.
    assert out[0]["churn_probability"] < out[1]["churn_probability"]


def test_predict_empty():
    assert predict([], model=None) == []
