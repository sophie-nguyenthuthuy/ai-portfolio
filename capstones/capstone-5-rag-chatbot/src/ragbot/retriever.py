"""Top-k retrieval with an optional lexical (BM25-ish) hybrid rerank.

The dense path embeds the query and searches the vector store. The optional
hybrid path blends the dense cosine score with a normalised lexical overlap
score so exact keyword matches (e.g. a policy term) are not lost to a fuzzy
dense backend. All implemented with base deps.
"""

from __future__ import annotations

import math
import re
from collections import Counter

from .config import Settings
from .embeddings import Embedder
from .logging_conf import get_logger
from .store import ScoredChunk, VectorStore

logger = get_logger(__name__)

_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def tokenize(text: str) -> list[str]:
    """Lower-case word tokenizer (Unicode-aware, Vietnamese-friendly)."""
    return _TOKEN_RE.findall(text.lower())


def _lexical_score(query_tokens: list[str], text: str) -> float:
    """A small BM25-flavoured term-frequency overlap score in [0, ~).

    Uses log-saturated term frequency over the query terms present in the
    candidate text. Normalised later across the candidate set.
    """
    if not query_tokens:
        return 0.0
    counts = Counter(tokenize(text))
    score = 0.0
    for term in set(query_tokens):
        tf = counts.get(term, 0)
        if tf:
            score += math.log1p(tf)
    return score


def _normalise(values: list[float]) -> list[float]:
    if not values:
        return values
    lo, hi = min(values), max(values)
    if hi - lo < 1e-12:
        return [0.0 for _ in values]
    return [(v - lo) / (hi - lo) for v in values]


class Retriever:
    """Embeds queries and retrieves relevant chunks from the vector store."""

    def __init__(self, embedder: Embedder, store: VectorStore, settings: Settings) -> None:
        self.embedder = embedder
        self.store = store
        self.settings = settings

    def retrieve(self, query: str, top_k: int | None = None) -> list[ScoredChunk]:
        """Return the top-k chunks for a query, optionally hybrid-reranked."""
        k = top_k or self.settings.top_k
        if not query.strip() or self.store.count() == 0:
            return []

        query_vec = self.embedder.embed([query])[0]
        # Over-fetch when reranking so lexical signal can promote candidates.
        fetch_k = k * 3 if self.settings.hybrid else k
        candidates = self.store.search(query_vec, top_k=fetch_k)
        if not candidates:
            return []

        if not self.settings.hybrid:
            return candidates[:k]

        query_tokens = tokenize(query)
        dense = _normalise([c.score for c in candidates])
        lexical = _normalise([_lexical_score(query_tokens, c.chunk.text) for c in candidates])
        alpha = self.settings.hybrid_alpha

        reranked: list[ScoredChunk] = []
        for cand, d, lx in zip(candidates, dense, lexical, strict=True):
            blended = alpha * d + (1.0 - alpha) * lx
            reranked.append(ScoredChunk(chunk=cand.chunk, score=blended))
        reranked.sort(key=lambda c: c.score, reverse=True)
        return reranked[:k]
