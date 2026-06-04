"""Shared fixtures: synthetic data, a trained model, and an API TestClient."""

from __future__ import annotations

import pytest

from churn.config import Settings
from churn.data import generate_synthetic
from churn.train import train_core


@pytest.fixture(scope="session")
def synth_df():
    return generate_synthetic(n=1500, seed=7)


@pytest.fixture(scope="session")
def settings(tmp_path_factory):
    """Settings pointing model artifacts at a temp dir (no repo pollution)."""
    tmp = tmp_path_factory.mktemp("models")
    return Settings(
        synthetic_rows=1500,
        random_seed=7,
        model_dir=str(tmp),
        classifier="logistic_regression",
    )


@pytest.fixture(scope="session")
def trained(settings):
    """A trained TrainResult (artifact persisted to the temp model dir)."""
    return train_core(settings, save=True)


@pytest.fixture
def client(trained):
    """FastAPI TestClient with the model preloaded (skips lifespan training)."""
    from fastapi.testclient import TestClient

    from churn.api import main as api_main

    api_main.STATE["model"] = trained.pipeline
    with TestClient(api_main.app) as c:
        yield c
    api_main.STATE["model"] = None
