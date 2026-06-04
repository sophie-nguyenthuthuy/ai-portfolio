"""Shared pytest fixtures: isolated model dir, synthetic data, TestClient."""

from __future__ import annotations

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from nlpvi import predict as predict_mod
from nlpvi.config import Settings, get_settings
from nlpvi.data import generate_synthetic


@pytest.fixture
def synthetic_df() -> pd.DataFrame:
    return generate_synthetic(120, seed=7)


@pytest.fixture
def settings(tmp_path) -> Settings:
    """Settings pointing at an isolated tmp model dir, MLflow disabled."""
    return Settings(
        model_dir=str(tmp_path),
        model_filename="sentiment.joblib",
        data_path=str(tmp_path / "nonexistent.csv"),
        synthetic_size=240,
        mlflow_enabled=False,
        random_seed=7,
    )


@pytest.fixture
def trained_model(settings):
    from nlpvi.train import train_model

    result = train_model(settings, use_mlflow=False)
    predict_mod.reset_cache()
    return settings, result


@pytest.fixture
def client(tmp_path, monkeypatch):
    """TestClient whose lifespan trains a tiny model in an isolated dir."""
    get_settings.cache_clear()
    monkeypatch.setenv("NLPVI_MODEL_DIR", str(tmp_path))
    monkeypatch.setenv("NLPVI_SYNTHETIC_SIZE", "240")
    monkeypatch.setenv("NLPVI_MLFLOW_ENABLED", "false")
    monkeypatch.setenv("NLPVI_RANDOM_SEED", "7")
    monkeypatch.setenv("NLPVI_DATA_PATH", str(tmp_path / "nonexistent.csv"))
    predict_mod.reset_cache()

    from nlpvi.api.main import create_app

    app = create_app()
    with TestClient(app) as c:
        yield c
    predict_mod.reset_cache()
    get_settings.cache_clear()
