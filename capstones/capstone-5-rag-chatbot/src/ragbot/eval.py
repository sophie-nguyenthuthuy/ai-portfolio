"""Lightweight, RAGAS-style offline evaluation implemented with base deps.

We do NOT depend on the `ragas` package (that path is an integration test). The
metrics here are deterministic and run on the FakeLLM + synthetic corpus:

  - context_precision  : fraction of questions whose expected source appears in
                         the retrieved chunks (retrieval correctness).
  - context_recall     : same expected-source hit but at the requested top_k
                         (here equal to precision proxy on a single-relevant set).
  - answer_groundedness: token overlap between the answer and retrieved context
                         (is the answer actually supported by what we fetched?).
  - answer_relevance   : token overlap between the answer and the question.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from typing import Any

from .config import Settings, get_settings
from .logging_conf import get_logger
from .pipeline import RAGPipeline
from .retriever import tokenize

logger = get_logger(__name__)


@dataclass
class EvalCase:
    """A single golden evaluation example."""

    question: str
    expected_source: str


# Golden set tied to the synthetic corpus shipped in data.py.
GOLDEN_SET: list[EvalCase] = [
    EvalCase("Nhan vien duoc bao nhieu ngay nghi phep?", "chinh_sach_nghi_phep.md"),
    EvalCase("Khach hang co the hoan tien trong bao lau?", "quy_trinh_hoan_tien.md"),
    EvalCase("Mat khau nguoi dung duoc luu nhu the nao?", "bao_mat_du_lieu.md"),
    EvalCase("Nhan vien moi duoc gan mentor trong bao lau?", "onboarding.md"),
]


def _overlap(a: str, b: str) -> float:
    """Jaccard-ish token overlap of `a` against `b` (recall of a in b)."""
    ta, tb = set(tokenize(a)), set(tokenize(b))
    if not ta:
        return 0.0
    return len(ta & tb) / len(ta)


def evaluate(
    pipeline: RAGPipeline,
    cases: list[EvalCase] | None = None,
    top_k: int | None = None,
) -> dict[str, Any]:
    """Score the pipeline over the golden set and return aggregate metrics."""
    cases = cases or GOLDEN_SET
    per_case: list[dict[str, Any]] = []
    precision_hits = 0
    groundedness_sum = 0.0
    relevance_sum = 0.0

    for case in cases:
        result = pipeline.answer(case.question, top_k=top_k)
        sources = result["sources"]
        retrieved_sources = [s["source"] for s in sources]
        hit = case.expected_source in retrieved_sources
        precision_hits += int(hit)

        context = " ".join(s["text"] for s in sources)
        grounded = _overlap(result["answer"], context)
        relevant = _overlap(result["answer"], case.question)
        groundedness_sum += grounded
        relevance_sum += relevant

        per_case.append(
            {
                "question": case.question,
                "expected_source": case.expected_source,
                "retrieved_sources": retrieved_sources,
                "hit": hit,
                "answer_groundedness": round(grounded, 4),
                "answer_relevance": round(relevant, 4),
            }
        )

    n = len(cases)
    metrics = {
        "context_precision": round(precision_hits / n, 4) if n else 0.0,
        "context_recall": round(precision_hits / n, 4) if n else 0.0,
        "answer_groundedness": round(groundedness_sum / n, 4) if n else 0.0,
        "answer_relevance": round(relevance_sum / n, 4) if n else 0.0,
        "n_cases": n,
    }
    logger.info("evaluation complete", extra={"metrics": metrics})
    return {"metrics": metrics, "cases": per_case}


def run_eval(settings: Settings | None = None) -> dict[str, Any]:
    """Build a pipeline on the sample corpus and evaluate it end-to-end."""
    settings = settings or get_settings()
    pipe = RAGPipeline(settings)
    pipe.ingest_sample_corpus()
    return evaluate(pipe)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Offline RAGAS-style RAG eval")
    parser.add_argument("--top-k", type=int, default=None)
    args = parser.parse_args(argv)

    settings = get_settings()
    pipe = RAGPipeline(settings)
    pipe.ingest_sample_corpus()
    report = evaluate(pipe, top_k=args.top_k)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
