"""Shared pytest fixtures: synthetic series, settings, TestClient.

Everything here is offline and uses the numpy/sklearn baseline model.
"""

from __future__ import annotations

import pandas as pd
import pytest
from fastapi.testclient import TestClient

from forecast.config import Settings
from forecast.data import generate_synthetic


@pytest.fixture
def synthetic_series() -> pd.Series:
    return generate_synthetic(n_days=400, seed=7)


@pytest.fixture
def settings(tmp_path) -> Settings:
    """Settings isolated to a temp dir; baseline model; mlflow off."""
    return Settings(
        data_path=str(tmp_path / "missing.csv"),  # forces synthetic fallback
        synthetic_days=400,
        seed=7,
        season_length=7,
        horizon=14,
        test_size=28,
        backtest_folds=2,
        model_name="baseline",
        model_dir=str(tmp_path / "models"),
        use_mlflow=False,
    )


@pytest.fixture
def client(monkeypatch, settings) -> TestClient:
    """TestClient whose app uses the isolated test Settings."""
    import forecast.api.main as api_main
    from forecast import config as config_mod

    monkeypatch.setattr(config_mod, "get_settings", lambda: settings)
    monkeypatch.setattr(api_main, "get_settings", lambda: settings)

    app = api_main.create_app()
    with TestClient(app) as c:
        yield c
