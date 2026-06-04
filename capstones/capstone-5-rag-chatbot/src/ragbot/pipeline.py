"""End-to-end RAG pipeline: ingest documents and answer questions with sources.

Wires together the configurable embedder, vector store, retriever and LLM. The
defaults (HashingEmbedder + InMemoryStore + FakeLLM) make the whole pipeline run
offline, which is what the test-suite and the API lifespan rely on.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .config import Settings, get_settings
from .data import Chunk, build_chunks, load_documents, synthetic_corpus
from .embeddings import Embedder, build_embedder
from .llm import LLMClient, build_llm, build_prompt
from .logging_conf import get_logger
from .retriever import Retriever
from .store import ScoredChunk, VectorStore, build_store

logger = get_logger(__name__)


class RAGPipeline:
    """Holds the configured components and exposes ingest/answer."""

    def __init__(
        self,
        settings: Settings | None = None,
        *,
        embedder: Embedder | None = None,
        store: VectorStore | None = None,
        llm: LLMClient | None = None,
    ) -> None:
        self.settings = settings or get_settings()
        self.embedder = embedder or build_embedder(self.settings)
        self.store = store or build_store(self.settings, self.embedder.dim)
        self.llm = llm or build_llm(self.settings)
        self.retriever = Retriever(self.embedder, self.store, self.settings)

    # --- ingestion ---------------------------------------------------------
    def ingest_texts(self, docs: dict[str, str]) -> int:
        """Chunk, embed and upsert a mapping of source -> text. Returns #chunks."""
        chunks = build_chunks(
            docs,
            chunk_size=self.settings.chunk_size,
            overlap=self.settings.chunk_overlap,
        )
        return self._upsert(chunks)

    def ingest(self, paths: list[str | Path]) -> int:
        """Load .txt/.md files (or dirs) from paths, then ingest them."""
        docs = load_documents(paths)
        if not docs:
            logger.warning("no supported documents found", extra={"paths": [str(p) for p in paths]})
            return 0
        return self.ingest_texts(docs)

    def ingest_sample_corpus(self) -> int:
        """Ingest the bundled sample docs dir, falling back to the synthetic set."""
        docs = load_documents([self.settings.resolved_sample_docs_dir])
        if not docs:
            logger.info("sample docs dir empty; using synthetic corpus")
            docs = synthetic_corpus()
        return self.ingest_texts(docs)

    def _upsert(self, chunks: list[Chunk]) -> int:
        if not chunks:
            return 0
        vectors = self.embedder.embed([c.text for c in chunks])
        n = self.store.upsert(chunks, vectors)
        logger.info("ingested chunks", extra={"chunks": n, "total": self.store.count()})
        return n

    # --- answering ---------------------------------------------------------
    def _build_context(self, retrieved: list[ScoredChunk]) -> str:
        """Concatenate retrieved chunks into a citation-numbered context block."""
        parts: list[str] = []
        budget = self.settings.max_context_chars
        used = 0
        for i, sc in enumerate(retrieved, start=1):
            snippet = f"[{i}] ({sc.chunk.source}) {sc.chunk.text}"
            if used + len(snippet) > budget and parts:
                break
            parts.append(snippet)
            used += len(snippet)
        return "\n\n".join(parts)

    def answer(self, question: str, top_k: int | None = None) -> dict[str, Any]:
        """Run RAG: retrieve -> build prompt -> LLM -> answer + cited sources."""
        retrieved = self.retriever.retrieve(question, top_k=top_k)
        if not retrieved:
            return {
                "answer": "Toi khong tim thay thong tin lien quan trong tai lieu.",
                "sources": [],
                "question": question,
            }

        context = self._build_context(retrieved)
        prompt = build_prompt(question, context)
        text = self.llm.generate(prompt)

        sources = [
            {
                "rank": i,
                "source": sc.chunk.source,
                "chunk_index": sc.chunk.chunk_index,
                "score": round(float(sc.score), 6),
                "text": sc.chunk.text,
            }
            for i, sc in enumerate(retrieved, start=1)
        ]
        return {"answer": text, "sources": sources, "question": question}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="RAG pipeline: ingest + ask")
    parser.add_argument("--paths", nargs="*", default=None, help="files/dirs to ingest")
    parser.add_argument("--question", default="Chinh sach nghi phep co bao nhieu ngay?")
    parser.add_argument("--top-k", type=int, default=None)
    args = parser.parse_args(argv)

    pipe = RAGPipeline()
    if args.paths:
        pipe.ingest([Path(p) for p in args.paths])
    else:
        pipe.ingest_sample_corpus()

    result = pipe.answer(args.question, top_k=args.top_k)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
