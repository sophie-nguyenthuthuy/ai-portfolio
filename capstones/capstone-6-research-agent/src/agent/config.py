"""Typed application settings (pydantic-settings), seeded from conf/config.yaml + env."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root = parent of src/agent/config.py -> src/agent -> src -> <root>
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONF_PATH = PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


class Settings(BaseSettings):
    """Runtime configuration. Env vars (prefix AGENT_) override yaml defaults."""

    model_config = SettingsConfigDict(
        env_prefix="AGENT_",
        env_file=".env",
        extra="ignore",
    )

    # --- general ---
    app_name: str = "research-agent"
    log_level: str = "INFO"

    # --- agent loop ---
    max_steps: int = 6
    # graph backend: "auto" picks langgraph if installed, else SimpleGraph.
    # one of: "auto", "langgraph", "simple"
    graph_backend: str = "auto"

    # --- llm ---
    # "fake" (deterministic, default/tests) or "ollama" (local network call)
    llm_backend: str = "fake"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"
    llm_timeout_s: float = 30.0

    # --- tools ---
    # "fake" (deterministic) or "tavily" (real, optional, never used in tests)
    search_backend: str = "fake"
    corpus_dir: str = "data/corpus"
    retriever_top_k: int = 3

    # --- api ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    @property
    def resolved_corpus_dir(self) -> Path:
        p = Path(self.corpus_dir)
        return p if p.is_absolute() else PROJECT_ROOT / p


@lru_cache
def get_settings() -> Settings:
    """Cached Settings instance built from yaml defaults + env overrides."""
    yaml_defaults = _load_yaml(CONF_PATH)
    return Settings(**yaml_defaults)
