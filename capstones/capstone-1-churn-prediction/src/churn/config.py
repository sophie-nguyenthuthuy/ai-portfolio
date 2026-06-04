"""Typed application settings (pydantic-settings), seeded from conf/config.yaml + env."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root = parent of src/churn/config.py -> src/churn -> src -> <root>
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONF_PATH = PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


class Settings(BaseSettings):
    """Runtime configuration. Env vars (prefix CHURN_) override yaml defaults."""

    model_config = SettingsConfigDict(
        env_prefix="CHURN_",
        env_file=".env",
        extra="ignore",
    )

    # --- general ---
    app_name: str = "churn-prediction"
    log_level: str = "INFO"

    # --- data ---
    data_path: str = "data/telco_churn.csv"
    synthetic_rows: int = 4000
    random_seed: int = 42
    test_size: float = 0.2

    # --- model ---
    # one of: "gradient_boosting", "logistic_regression", "xgboost" (optional dep)
    classifier: str = "gradient_boosting"
    model_dir: str = "models"
    model_filename: str = "churn-model.joblib"

    # --- mlflow ---
    mlflow_tracking_uri: str = "./mlruns"
    mlflow_experiment: str = "churn-prediction"

    # --- api ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    @property
    def model_path(self) -> Path:
        return PROJECT_ROOT / self.model_dir / self.model_filename

    @property
    def metadata_path(self) -> Path:
        return self.model_path.with_suffix(".meta.json")

    @property
    def resolved_data_path(self) -> Path:
        p = Path(self.data_path)
        return p if p.is_absolute() else PROJECT_ROOT / p


@lru_cache
def get_settings() -> Settings:
    """Cached Settings instance built from yaml defaults + env overrides."""
    yaml_defaults = _load_yaml(CONF_PATH)
    return Settings(**yaml_defaults)
