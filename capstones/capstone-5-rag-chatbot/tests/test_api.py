"""API tests: health/ready/metrics plus /chat and /ingest via TestClient."""

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
    body = r.json()
    assert body["status"] == "ready"
    assert body["chunks_indexed"] > 0


def test_metrics(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_request" in r.text or "process_" in r.text


def test_chat_returns_answer_and_sources(client):
    r = client.post("/chat", json={"question": "Nhan vien duoc bao nhieu ngay nghi phep?"})
    assert r.status_code == 200
    body = r.json()
    assert body["answer"]
    assert body["sources"]
    assert "chinh_sach_nghi_phep.md" in [s["source"] for s in body["sources"]]


def test_chat_top_k_override(client):
    r = client.post("/chat", json={"question": "bao mat du lieu", "top_k": 2})
    assert r.status_code == 200
    assert len(r.json()["sources"]) <= 2


def test_chat_validation_error(client):
    r = client.post("/chat", json={"question": ""})
    assert r.status_code == 422


def test_ingest_inline_documents(client):
    r = client.post("/ingest", json={"documents": {"policy.md": "Cong ty nghi le vao thu bay."}})
    assert r.status_code == 200
    body = r.json()
    assert body["ingested_chunks"] >= 1
    # The newly ingested doc is now retrievable.
    chat = client.post("/chat", json={"question": "Cong ty nghi le khi nao?"})
    assert "policy.md" in [s["source"] for s in chat.json()["sources"]]


def test_ingest_requires_payload(client):
    r = client.post("/ingest", json={})
    assert r.status_code == 422
