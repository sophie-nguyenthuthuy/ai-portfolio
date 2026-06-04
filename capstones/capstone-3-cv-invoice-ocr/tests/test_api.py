"""API tests via TestClient: health/ready/metrics + classify + ocr uploads."""

from __future__ import annotations


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["app"] == "cv-invoice-ocr"
    assert "version" in body


def test_ready_reports_loaded_model(client):
    resp = client.get("/ready")
    assert resp.status_code == 200
    body = resp.json()
    assert body["ready"] is True
    assert body["model_loaded"] is True
    assert body["backend"] == "dummy"
    assert set(body["labels"]) == {"invoice", "receipt", "id_card", "other"}


def test_metrics_endpoint(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "http_request" in resp.text


def test_classify_upload(client, image_bytes_for):
    data = image_bytes_for("invoice", size=48, seed=1)
    resp = client.post(
        "/classify",
        files={"file": ("invoice.png", data, "image/png")},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["label"] in {"invoice", "receipt", "id_card", "other"}
    assert 0.0 <= body["confidence"] <= 1.0
    assert body["backend"] == "dummy"
    assert body["label"] == "invoice"


def test_ocr_upload(client, image_bytes_for):
    data = image_bytes_for("invoice", size=48, seed=0)
    resp = client.post(
        "/ocr",
        files={"file": ("invoice.png", data, "image/png")},
    )
    assert resp.status_code == 200
    body = resp.json()
    assert body["engine"] == "stub"
    assert body["fields"]["invoice_no"] == "INV-2026-0042"
    assert body["fields"]["total"] is not None


def test_classify_empty_upload_rejected(client):
    resp = client.post(
        "/classify",
        files={"file": ("empty.png", b"", "image/png")},
    )
    assert resp.status_code == 400
