"""Vector stores behind a small protocol.

`InMemoryStore` (default/tests) keeps vectors in a numpy matrix and does an exact
cosine-similarity search — zero external services, fully offline. `QdrantStore`
is an OPTIONAL backend that lazily imports `qdrant-client` only when selected.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable

import numpy as np

from .config import Settings
from .data import Chunk
from .logging_conf import get_logger

logger = get_logger(__name__)


@dataclass
class ScoredChunk:
    """A retrieved chunk plus its similarity score."""

    chunk: Chunk
    score: float

    def to_dict(self) -> dict[str, Any]:
        return {**self.chunk.to_dict(), "score": round(float(self.score), 6)}


@runtime_checkable
class VectorStore(Protocol):
    """Upsert chunk vectors and search by a query vector."""

    def upsert(self, chunks: list[Chunk], vectors: np.ndarray) -> int: ...

    def search(self, query_vector: np.ndarray, top_k: int) -> list[ScoredChunk]: ...

    def count(self) -> int: ...

    def reset(self) -> None: ...


class InMemoryStore:
    """Exact cosine-similarity store backed by a numpy matrix.

    Vectors are expected pre-normalised (the embedders L2-normalise), so a plain
    dot product is the cosine similarity. Upserts dedupe by chunk id.
    """

    def __init__(self, dim: int) -> None:
        self.dim = int(dim)
        self._chunks: list[Chunk] = []
        self._ids: dict[str, int] = {}
        self._matrix = np.zeros((0, self.dim), dtype=np.float32)

    def upsert(self, chunks: list[Chunk], vectors: np.ndarray) -> int:
        if len(chunks) != vectors.shape[0]:
            raise ValueError("chunks and vectors length mismatch")
        if vectors.size and vectors.shape[1] != self.dim:
            raise ValueError(f"expected dim {self.dim}, got {vectors.shape[1]}")

        rows: list[np.ndarray] = []
        for chunk, vec in zip(chunks, vectors, strict=True):
            if chunk.id in self._ids:  # overwrite existing row in place
                self._matrix[self._ids[chunk.id]] = vec
                self._chunks[self._ids[chunk.id]] = chunk
                continue
            self._ids[chunk.id] = len(self._chunks)
            self._chunks.append(chunk)
            rows.append(np.asarray(vec, dtype=np.float32))
        if rows:
            self._matrix = np.vstack([self._matrix, np.vstack(rows)])
        return len(chunks)

    def search(self, query_vector: np.ndarray, top_k: int) -> list[ScoredChunk]:
        if self._matrix.shape[0] == 0 or top_k <= 0:
            return []
        q = np.asarray(query_vector, dtype=np.float32).reshape(-1)
        scores = self._matrix @ q
        k = min(top_k, scores.shape[0])
        # argpartition for the top-k, then sort just those by score desc.
        idx = np.argpartition(-scores, k - 1)[:k]
        idx = idx[np.argsort(-scores[idx])]
        return [ScoredChunk(chunk=self._chunks[i], score=float(scores[i])) for i in idx]

    def count(self) -> int:
        return len(self._chunks)

    def reset(self) -> None:
        self._chunks = []
        self._ids = {}
        self._matrix = np.zeros((0, self.dim), dtype=np.float32)


class QdrantStore:
    """OPTIONAL Qdrant-backed store (lazy import of qdrant-client)."""

    def __init__(self, url: str, collection: str, dim: int) -> None:  # pragma: no cover - optional
        try:
            from qdrant_client import QdrantClient
            from qdrant_client.models import Distance, VectorParams
        except ImportError as exc:
            raise ImportError(
                "qdrant-client not installed; install '.[qdrant]' "
                "or set RAGBOT_VECTOR_STORE=memory"
            ) from exc
        self.dim = int(dim)
        self.collection = collection
        self._client = QdrantClient(url=url)
        self._models = __import__("qdrant_client.models", fromlist=["models"])
        if not self._client.collection_exists(collection):
            self._client.create_collection(
                collection_name=collection,
                vectors_config=VectorParams(size=self.dim, distance=Distance.COSINE),
            )

    def upsert(self, chunks: list[Chunk], vectors: np.ndarray) -> int:  # pragma: no cover - optional
        from qdrant_client.models import PointStruct

        points = [
            PointStruct(
                id=abs(hash(c.id)) % (2**63),
                vector=vec.tolist(),
                payload=c.to_dict(),
            )
            for c, vec in zip(chunks, vectors, strict=True)
        ]
        self._client.upsert(collection_name=self.collection, points=points)
        return len(points)

    def search(self, query_vector: np.ndarray, top_k: int) -> list[ScoredChunk]:  # pragma: no cover
        hits = self._client.search(
            collection_name=self.collection,
            query_vector=np.asarray(query_vector, dtype=np.float32).reshape(-1).tolist(),
            limit=top_k,
        )
        out: list[ScoredChunk] = []
        for h in hits:
            payload = h.payload or {}
            out.append(
                ScoredChunk(
                    chunk=Chunk(
                        id=str(payload.get("id", h.id)),
                        text=payload.get("text", ""),
                        source=payload.get("source", ""),
                        chunk_index=int(payload.get("chunk_index", 0)),
                        metadata=payload.get("metadata", {}),
                    ),
                    score=float(h.score),
                )
            )
        return out

    def count(self) -> int:  # pragma: no cover - optional
        return int(self._client.count(self.collection).count)

    def reset(self) -> None:  # pragma: no cover - optional
        self._client.delete_collection(self.collection)


def build_store(settings: Settings, dim: int) -> VectorStore:
    """Factory: pick the vector store from settings (default in-memory)."""
    kind = settings.vector_store.lower()
    if kind in {"memory", "inmemory", "numpy"}:
        logger.info("using InMemoryStore", extra={"dim": dim})
        return InMemoryStore(dim=dim)
    if kind == "qdrant":
        logger.info("using QdrantStore", extra={"url": settings.qdrant_url})
        return QdrantStore(settings.qdrant_url, settings.collection, dim)
    raise ValueError(f"unknown vector_store: {settings.vector_store!r}")
