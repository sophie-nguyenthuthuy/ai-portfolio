"""Shared pytest fixtures: synthetic images, a trained dummy model, TestClient.

Everything here is offline and CPU-only. The classifier defaults to the numpy
``DummyClassifier`` (torch not installed) and OCR uses the deterministic stub.
"""

from __future__ import annotations

import io
from pathlib import Path

import pytest

from vision.config import Settings
from vision.data import build_synthetic_dataset, generate_synthetic_image


@pytest.fixture(scope="session")
def labels() -> list[str]:
    return ["invoice", "receipt", "id_card", "other"]


@pytest.fixture
def settings(tmp_path: Path, labels: list[str]) -> Settings:
    """Settings pointed at a temp model dir so tests never touch real artifacts."""
    return Settings(
        data_path=str(tmp_path / "data"),
        model_dir=str(tmp_path / "models"),
        labels=labels,
        samples_per_class=12,
        image_size=48,
        backend="dummy",
        ocr_engine="stub",
        use_mlflow=False,
        epochs=1,
    )


@pytest.fixture
def image_bytes_for():
    """Factory: ``image_bytes_for("invoice")`` -> PNG bytes for that class."""

    def _make(label: str, *, size: int = 48, seed: int = 0) -> bytes:
        img = generate_synthetic_image(label, size=size, seed=seed)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        return buf.getvalue()

    return _make


@pytest.fixture
def synthetic_dataset(labels: list[str]):
    return build_synthetic_dataset(labels, samples_per_class=12, size=48, seed=42)


@pytest.fixture
def trained_dummy(settings: Settings):
    """A DummyClassifier trained via the real pipeline on synthetic data."""
    from vision.pipeline import train_pipeline

    return train_pipeline(settings, backend="dummy", save=True)


@pytest.fixture
def client(settings: Settings, monkeypatch):
    """FastAPI TestClient with get_settings patched to the temp settings."""
    import vision.api.main as api_main
    from fastapi.testclient import TestClient

    monkeypatch.setattr(api_main, "get_settings", lambda: settings)
    monkeypatch.setattr("vision.predict.get_settings", lambda: settings)

    app = api_main.create_app()
    with TestClient(app) as c:
        yield c
