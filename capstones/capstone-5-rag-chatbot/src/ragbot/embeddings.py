"""Embedding backends behind a small protocol.

`HashingEmbedder` (base deps only, default) uses sklearn's HashingVectorizer so
tests embed text deterministically with no model download. `SentenceTransformer
Embedder` is an OPTIONAL backend imported lazily only when selected.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable

import numpy as np

from .config import Settings
from .logging_conf import get_logger

logger = get_logger(__name__)


@runtime_checkable
class Embedder(Protocol):
    """Maps a batch of texts to a (n, dim) float32 matrix of unit vectors."""

    dim: int

    def embed(self, texts: list[str]) -> np.ndarray: ...


def _l2_normalise(matrix: np.ndarray) -> np.ndarray:
    """Row-wise L2 normalisation so dot product == cosine similarity."""
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    norms[norms == 0.0] = 1.0
    return (matrix / norms).astype(np.float32)


class HashingEmbedder:
    """Deterministic embeddings via the hashing trick (no training, no download).

    Each text is hashed into a fixed-dim sparse bag-of-words vector, then L2
    normalised. Cosine similarity over these vectors gives a usable lexical-ish
    dense signal that is fully reproducible offline.
    """

    def __init__(self, dim: int = 512) -> None:
        self.dim = int(dim)
        # Lazy local import keeps module import light; sklearn is a base dep.
        from sklearn.feature_extraction.text import HashingVectorizer

        self._vectorizer = HashingVectorizer(
            n_features=self.dim,
            alternate_sign=False,
            norm=None,
            analyzer="word",
            ngram_range=(1, 2),
        )

    def embed(self, texts: list[str]) -> np.ndarray:
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        sparse = self._vectorizer.transform(texts)
        dense = np.asarray(sparse.todense(), dtype=np.float32)
        return _l2_normalise(dense)


class SentenceTransformerEmbedder:
    """OPTIONAL semantic embeddings via sentence-transformers (lazy import)."""

    def __init__(self, model_name: str) -> None:
        try:
            from sentence_transformers import SentenceTransformer  # lazy optional
        except ImportError as exc:  # pragma: no cover - exercised only with extra
            raise ImportError(
                "sentence-transformers not installed; "
                "install '.[st]' or set RAGBOT_EMBEDDER=hashing"
            ) from exc
        self._model = SentenceTransformer(model_name)
        self.dim = int(self._model.get_sentence_embedding_dimension())

    def embed(self, texts: list[str]) -> np.ndarray:  # pragma: no cover - optional
        if not texts:
            return np.zeros((0, self.dim), dtype=np.float32)
        vecs = self._model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
        return np.asarray(vecs, dtype=np.float32)


def build_embedder(settings: Settings) -> Embedder:
    """Factory: pick the embedding backend from settings (default hashing)."""
    kind = settings.embedder.lower()
    if kind in {"hashing", "hash"}:
        logger.info("using HashingEmbedder", extra={"dim": settings.embedding_dim})
        return HashingEmbedder(dim=settings.embedding_dim)
    if kind in {"sentence-transformers", "st", "sbert"}:
        logger.info("using SentenceTransformerEmbedder", extra={"model": settings.st_model_name})
        return SentenceTransformerEmbedder(settings.st_model_name)
    raise ValueError(f"unknown embedder: {settings.embedder!r}")
