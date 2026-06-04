"""Typed application settings (pydantic-settings), seeded from conf/config.yaml + env."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root = parent of src/mlops/config.py -> src/mlops -> src -> <root>
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONF_PATH = PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


class Settings(BaseSettings):
    """Runtime configuration. Env vars (prefix MLOPS_) override yaml defaults."""

    model_config = SettingsConfigDict(
        env_prefix="MLOPS_",
        env_file=".env",
        extra="ignore",
    )

    # --- general ---
    app_name: str = "mlops-platform"
    model_name: str = "churn-reference"
    log_level: str = "INFO"

    # --- data ---
    data_path: str = "data/reference.csv"
    synthetic_rows: int = 4000
    random_seed: int = 42
    test_size: float = 0.2

    # --- model ---
    # one of: "gradient_boosting", "logistic_regression"
    classifier: str = "gradient_boosting"

    # --- pipeline / orchestration ---
    # one of: "base" (built-in DAG runner) | "prefect" (optional dep, lazy import)
    pipeline_backend: str = "base"
    # gate the deploy-check stage on this metric floor
    min_roc_auc: float = 0.7

    # --- registry ---
    # one of: "local" (versioned joblib + JSON manifest) | "mlflow" (optional, lazy)
    registry_backend: str = "local"
    registry_dir: str = "registry"

    # --- mlflow (optional path) ---
    mlflow_tracking_uri: str = "./mlruns"
    mlflow_experiment: str = "mlops-platform"

    # --- monitoring ---
    drift_threshold: float = 0.25

    # --- api ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    @property
    def resolved_registry_dir(self) -> Path:
        p = Path(self.registry_dir)
        return p if p.is_absolute() else PROJECT_ROOT / p

    @property
    def resolved_data_path(self) -> Path:
        p = Path(self.data_path)
        return p if p.is_absolute() else PROJECT_ROOT / p


@lru_cache
def get_settings() -> Settings:
    """Cached Settings instance built from yaml defaults + env overrides."""
    yaml_defaults = _load_yaml(CONF_PATH)
    return Settings(**yaml_defaults)
