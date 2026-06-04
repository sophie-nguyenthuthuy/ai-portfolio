"""Typed application settings (pydantic-settings).

Values resolve from, in order: environment variables (prefix ``NLPVI_``),
then ``conf/config.yaml``, then the in-code defaults below.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if path.exists():
        with path.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh) or {}
        if not isinstance(data, dict):
            raise ValueError(f"config yaml must be a mapping: {path}")
        return data
    return {}


class Settings(BaseSettings):
    """Runtime configuration for training and serving."""

    model_config = SettingsConfigDict(
        env_prefix="NLPVI_",
        env_file=".env",
        extra="ignore",
        protected_namespaces=(),
    )

    # general
    app_name: str = "nlpvi"
    log_level: str = "INFO"
    random_seed: int = 13

    # model selection
    model_backend: Literal["sklearn", "phobert"] = "sklearn"
    phobert_model_name: str = "vinai/phobert-base"
    max_seq_len: int = 128

    # data
    data_path: str = "data/reviews.csv"
    synthetic_size: int = 600
    test_size: float = 0.2

    # tf-idf + lr hyperparameters
    tfidf_max_features: int = 5000
    tfidf_ngram_max: int = 2
    lr_c: float = 4.0
    lr_max_iter: int = 1000

    # artifacts
    model_dir: str = "models"
    model_filename: str = "sentiment.joblib"

    # mlflow
    mlflow_enabled: bool = True
    mlflow_tracking_uri: str = "file:./mlruns"
    mlflow_experiment: str = "nlpvi-sentiment"

    # serving
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    seed: int = Field(default=13, exclude=True)

    @property
    def model_path(self) -> Path:
        return PROJECT_ROOT / self.model_dir / self.model_filename


@lru_cache
def get_settings(config_path: str | None = None) -> Settings:
    """Build cached Settings, layering yaml defaults under env overrides."""
    path = Path(config_path) if config_path else DEFAULT_CONFIG
    file_values = _load_yaml(path)
    return Settings(**file_values)
