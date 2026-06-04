"""PSI drift monitor for RAG query/retrieval distributions, with a CLI.

In a RAG service the things that drift are not tabular features but the *query
distribution* (e.g. query length) and the *retrieval-score distribution* (how
confidently the store matches incoming questions). A sustained shift signals the
incoming traffic no longer resembles the indexed corpus -> reindex / re-embed.

PSI rule of thumb:
  < 0.1   : no significant population change
  0.1-0.25: moderate change (investigate)
  > 0.25  : significant change (likely re-ingest / re-embed)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

# Allow running both as a module and as a script.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ragbot.retriever import tokenize  # noqa: E402


def psi(
    reference: np.ndarray,
    current: np.ndarray,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Compute PSI between a reference and current 1-D numeric distribution.

    Bin edges are derived from quantiles of the reference distribution.
    """
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    ref = ref[~np.isnan(ref)]
    cur = cur[~np.isnan(cur)]
    if ref.size == 0 or cur.size == 0:
        return 0.0

    quantiles = np.linspace(0, 1, bins + 1)
    edges = np.unique(np.quantile(ref, quantiles))
    if edges.size < 2:  # degenerate (constant) distribution
        return 0.0
    edges[0], edges[-1] = -np.inf, np.inf

    ref_counts, _ = np.histogram(ref, bins=edges)
    cur_counts, _ = np.histogram(cur, bins=edges)

    ref_pct = ref_counts / ref_counts.sum() + epsilon
    cur_pct = cur_counts / cur_counts.sum() + epsilon

    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def query_length_psi(
    reference_queries: list[str],
    current_queries: list[str],
    bins: int = 10,
) -> float:
    """PSI over query *token length* between two batches of queries."""
    ref = np.array([len(tokenize(q)) for q in reference_queries], dtype=float)
    cur = np.array([len(tokenize(q)) for q in current_queries], dtype=float)
    return psi(ref, cur, bins=bins)


def score_psi(
    reference_scores: list[float],
    current_scores: list[float],
    bins: int = 10,
) -> float:
    """PSI over the top-1 retrieval-score distribution between two batches."""
    return psi(np.asarray(reference_scores), np.asarray(current_scores), bins=bins)


def evaluate_drift(scores: dict[str, float], threshold: float = 0.25) -> dict[str, object]:
    """Summarize PSI scores against a drift threshold."""
    drifted = {c: s for c, s in scores.items() if s > threshold}
    return {
        "psi": scores,
        "threshold": threshold,
        "drifted_signals": sorted(drifted),
        "drift_detected": bool(drifted),
        "max_psi": max(scores.values()) if scores else 0.0,
    }


def _demo() -> dict[str, object]:
    """Reference = short well-matched queries, current = long off-topic ones."""
    rng = np.random.default_rng(0)
    ref_q = ["nghi phep bao nhieu ngay" for _ in range(200)]
    cur_q = ["toi muon hoi mot cau hoi rat dai va lan man ve nhieu chu de" for _ in range(200)]
    ref_s = rng.normal(0.8, 0.05, 200).tolist()
    cur_s = rng.normal(0.4, 0.1, 200).tolist()
    return evaluate_drift(
        {
            "query_length": query_length_psi(ref_q, cur_q),
            "retrieval_score": score_psi(ref_s, cur_s),
        }
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="PSI drift check for RAG queries")
    parser.add_argument("--reference", type=Path, help="reference queries (one per line)")
    parser.add_argument("--current", type=Path, help="current queries (one per line)")
    parser.add_argument("--threshold", type=float, default=0.25)
    parser.add_argument("--bins", type=int, default=10)
    args = parser.parse_args(argv)

    if args.reference and args.current:
        ref_q = args.reference.read_text(encoding="utf-8").splitlines()
        cur_q = args.current.read_text(encoding="utf-8").splitlines()
        summary = evaluate_drift(
            {"query_length": query_length_psi(ref_q, cur_q, bins=args.bins)},
            threshold=args.threshold,
        )
    else:
        summary = _demo()

    print(json.dumps(summary, indent=2))
    return 1 if summary["drift_detected"] else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
