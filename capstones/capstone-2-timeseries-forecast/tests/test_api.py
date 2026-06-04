"""API tests via TestClient: health/ready/metrics + a real forecast call."""

from __future__ import annotations


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_ready_after_startup(client):
    r = client.get("/ready")
    assert r.status_code == 200
    body = r.json()
    assert body["ready"] is True
    assert body["model_loaded"] is True


def test_metrics_endpoint(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_request" in r.text or "process" in r.text


def test_forecast_endpoint(client):
    r = client.post("/forecast", json={"horizon": 7})
    assert r.status_code == 200
    body = r.json()
    assert body["horizon"] == 7
    assert len(body["points"]) == 7
    pt = body["points"][0]
    assert pt["yhat_lower"] <= pt["yhat"] <= pt["yhat_upper"]
    assert "model_name" in body


def test_forecast_validation(client):
    r = client.post("/forecast", json={"horizon": 0})
    assert r.status_code == 422
