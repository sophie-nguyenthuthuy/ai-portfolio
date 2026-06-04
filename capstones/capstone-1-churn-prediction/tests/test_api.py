"""API tests: health/ready/metrics plus single + batch predict via TestClient."""

from __future__ import annotations


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_ready(client):
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json()["model_loaded"] is True


def test_metrics(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_request" in r.text or "process_" in r.text


def test_predict_single(client):
    record = {
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
    r = client.post("/predict", json=record)
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 1
    p = body["predictions"][0]
    assert 0.0 <= p["churn_probability"] <= 1.0
    assert p["churn_label"] in (0, 1)


def test_predict_batch(client):
    records = [
        {
            "tenure": 70,
            "monthly_charges": 25.0,
            "total_charges": 1750.0,
            "num_services": 1,
            "senior_citizen": 0,
            "contract": "two-year",
            "payment_method": "credit-card",
            "internet_service": "none",
            "paperless_billing": "no",
            "gender": "male",
        },
        {
            "tenure": 1,
            "monthly_charges": 105.0,
            "total_charges": 105.0,
            "num_services": 5,
            "senior_citizen": 1,
            "contract": "month-to-month",
            "payment_method": "electronic-check",
            "internet_service": "fiber-optic",
            "paperless_billing": "yes",
            "gender": "female",
        },
    ]
    r = client.post("/predict", json=records)
    assert r.status_code == 200
    body = r.json()
    assert body["count"] == 2


def test_predict_validation_error(client):
    r = client.post("/predict", json={"tenure": -5})
    assert r.status_code == 422
