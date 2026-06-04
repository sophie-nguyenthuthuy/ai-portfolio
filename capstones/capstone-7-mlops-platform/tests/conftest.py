"""Shared fixtures: temp-dir Settings, synthetic data, registry, API TestClient.

All fixtures use the base-deps backends (LocalRegistry + base DAG runner) and
point storage at a temp dir so the repo is never polluted by the test run.
"""

from __future__ import annotations

import pytest

from mlops.config import Settings
from mlops.data import generate_synthetic


@pytest.fixture(scope="session")
def synth_df():
    return generate_synthetic(n=1500, seed=7)


@pytest.fixture
def settings(tmp_path):
    """Settings with registry storage in a temp dir; fast logistic model."""
    return Settings(
        synthetic_rows=1500,
        random_seed=7,
        classifier="logistic_regression",
        registry_backend="local",
        registry_dir=str(tmp_path / "registry"),
        pipeline_backend="base",
        min_roc_auc=0.7,
    )


@pytest.fixture
def registry(settings):
    from mlops.registry import get_registry

    return get_registry(settings)


@pytest.fixture
def trained_pipeline(settings, synth_df):
    """A fitted reference pipeline (not yet registered)."""
    from mlops.train import train_core

    return train_core(settings, df=synth_df)


@pytest.fixture
def client(trained_pipeline):
    """FastAPI TestClient with a model preloaded (skips lifespan bootstrap)."""
    from fastapi.testclient import TestClient

    from mlops.api import main as api_main

    api_main.STATE.update(
        {
            "model": trained_pipeline.pipeline,
            "version": 1,
            "stage": "Production",
            "metrics": trained_pipeline.metrics,
        }
    )
    with TestClient(api_main.app) as c:
        yield c
    api_main.STATE.update({"model": None, "version": None, "stage": None, "metrics": {}})
