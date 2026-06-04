"""API tests: health/ready/metrics plus a real /run call via TestClient."""

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
    assert r.json()["graph_loaded"] is True


def test_metrics(client):
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "http_request" in r.text or "process_" in r.text


def test_run_knowledge_question(client):
    r = client.post("/run", json={"question": "What is retrieval augmented generation?"})
    assert r.status_code == 200
    body = r.json()
    assert body["answer"]
    assert body["steps"] >= 1
    assert body["backend"] == "simple"
    assert any(c["tool"] == "retriever" for c in body["tool_calls"])


def test_run_arithmetic_question(client):
    r = client.post("/run", json={"question": "What is 6 * 7?", "max_steps": 4})
    assert r.status_code == 200
    body = r.json()
    assert "42" in body["answer"]
    assert any(c["tool"] == "calculator" for c in body["tool_calls"])


def test_run_validation_error(client):
    r = client.post("/run", json={"question": ""})
    assert r.status_code == 422
