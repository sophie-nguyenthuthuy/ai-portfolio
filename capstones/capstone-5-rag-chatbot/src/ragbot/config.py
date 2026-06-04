"""Typed application settings (pydantic-settings), seeded from conf/config.yaml + env."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root = parent of src/ragbot/config.py -> src/ragbot -> src -> <root>
PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONF_PATH = PROJECT_ROOT / "conf" / "config.yaml"


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


class Settings(BaseSettings):
    """Runtime configuration. Env vars (prefix RAGBOT_) override yaml defaults."""

    model_config = SettingsConfigDict(
        env_prefix="RAGBOT_",
        env_file=".env",
        extra="ignore",
    )

    # --- general ---
    app_name: str = "rag-chatbot"
    log_level: str = "INFO"
    random_seed: int = 42

    # --- corpus / ingestion ---
    # Folder holding the bundled sample corpus shipped with the repo.
    sample_docs_dir: str = "data/sample_docs"
    chunk_size: int = 400  # characters per chunk
    chunk_overlap: int = 80  # character overlap between adjacent chunks

    # --- embeddings ---
    # one of: "hashing" (base dep, default) | "sentence-transformers" (optional)
    embedder: str = "hashing"
    embedding_dim: int = 512
    st_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"

    # --- vector store ---
    # one of: "memory" (base dep, default) | "qdrant" (optional dep)
    vector_store: str = "memory"
    collection: str = "sme_docs"
    qdrant_url: str = "http://localhost:6333"

    # --- retrieval ---
    top_k: int = 4
    hybrid: bool = True  # blend dense cosine with a lexical keyword score
    hybrid_alpha: float = 0.7  # weight on dense score (1 - alpha on lexical)

    # --- llm (Ollama) ---
    # one of: "fake" (deterministic, default/tests) | "ollama"
    llm: str = "fake"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1"
    llm_timeout: float = 60.0
    max_context_chars: int = 2000

    # --- api ---
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    @property
    def resolved_sample_docs_dir(self) -> Path:
        p = Path(self.sample_docs_dir)
        return p if p.is_absolute() else PROJECT_ROOT / p


@lru_cache
def get_settings() -> Settings:
    """Cached Settings instance built from yaml defaults + env overrides."""
    yaml_defaults = _load_yaml(CONF_PATH)
    return Settings(**yaml_defaults)
