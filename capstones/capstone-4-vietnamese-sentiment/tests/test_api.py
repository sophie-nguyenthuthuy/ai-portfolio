"""API smoke tests via TestClient (model trained in lifespan)."""

from __future__ import annotations


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert "version" in body


def test_ready(client):
    resp = client.get("/ready")
    assert resp.status_code == 200
    assert resp.json()["ready"] is True


def test_metrics_exposed(client):
    resp = client.get("/metrics")
    assert resp.status_code == 200
    assert "http_request" in resp.text


def test_sentiment_predict(client):
    payload = {
        "texts": [
            "Sản phẩm tuyệt vời, giao hàng nhanh, rất đáng tiền",
            "Hàng tệ hại, kém chất lượng, rất thất vọng",
        ]
    }
    resp = client.post("/sentiment", json=payload)
    assert resp.status_code == 200
    body = resp.json()
    preds = body["predictions"]
    assert len(preds) == 2
    assert preds[0]["label"] == "positive"
    assert preds[1]["label"] == "negative"
    assert set(preds[0]["scores"].keys()) == {"negative", "neutral", "positive"}


def test_sentiment_empty_rejected(client):
    resp = client.post("/sentiment", json={"texts": []})
    assert resp.status_code == 422
