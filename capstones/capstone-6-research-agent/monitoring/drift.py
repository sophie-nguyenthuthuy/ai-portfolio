"""Behavioral drift for the research agent: step-count + tool-usage PSI, with CLI.

Two complementary checks:
  * step-count PSI  — numeric distribution of steps-per-run (binned).
  * tool-usage PSI  — categorical distribution of which tools get called.

PSI rule of thumb:
  < 0.1   : no significant change
  0.1-0.25: moderate change (investigate)
  > 0.25  : significant change (likely regression)
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from collections.abc import Iterable, Sequence

import numpy as np


def psi(
    reference: Sequence[float] | np.ndarray,
    current: Sequence[float] | np.ndarray,
    bins: int = 10,
    epsilon: float = 1e-6,
) -> float:
    """Population Stability Index between two 1-D numeric distributions.

    Bin edges come from quantiles of the reference distribution.
    """
    ref = np.asarray(reference, dtype=float)
    cur = np.asarray(current, dtype=float)
    ref = ref[~np.isnan(ref)]
    cur = cur[~np.isnan(cur)]
    if ref.size == 0 or cur.size == 0:
        return 0.0

    quantiles = np.linspace(0, 1, bins + 1)
    edges = np.unique(np.quantile(ref, quantiles))
    if edges.size < 2:  # degenerate (constant) feature
        return 0.0
    edges[0], edges[-1] = -np.inf, np.inf

    ref_counts, _ = np.histogram(ref, bins=edges)
    cur_counts, _ = np.histogram(cur, bins=edges)

    ref_pct = ref_counts / ref_counts.sum() + epsilon
    cur_pct = cur_counts / cur_counts.sum() + epsilon

    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def categorical_psi(
    reference: Iterable[str],
    current: Iterable[str],
    epsilon: float = 1e-6,
) -> float:
    """PSI over a categorical distribution (e.g. tool names)."""
    ref_counts = Counter(reference)
    cur_counts = Counter(current)
    categories = sorted(set(ref_counts) | set(cur_counts))
    if not categories:
        return 0.0

    ref_total = sum(ref_counts.values()) or 1
    cur_total = sum(cur_counts.values()) or 1

    total = 0.0
    for cat in categories:
        ref_pct = ref_counts.get(cat, 0) / ref_total + epsilon
        cur_pct = cur_counts.get(cat, 0) / cur_total + epsilon
        total += (cur_pct - ref_pct) * np.log(cur_pct / ref_pct)
    return float(total)


def step_count_psi(
    reference_steps: Sequence[float],
    current_steps: Sequence[float],
    bins: int = 10,
) -> float:
    """Convenience wrapper: PSI over steps-per-run."""
    return psi(reference_steps, current_steps, bins=bins)


def tool_usage_psi(
    reference_tools: Iterable[str],
    current_tools: Iterable[str],
) -> float:
    """Convenience wrapper: PSI over the flattened tool-name stream."""
    return categorical_psi(reference_tools, current_tools)


def evaluate_drift(scores: dict[str, float], threshold: float = 0.25) -> dict[str, object]:
    """Summarize named PSI scores against a drift threshold."""
    drifted = {k: v for k, v in scores.items() if v > threshold}
    return {
        "psi": scores,
        "threshold": threshold,
        "drifted_signals": sorted(drifted),
        "drift_detected": bool(drifted),
        "max_psi": max(scores.values()) if scores else 0.0,
    }


def _demo() -> dict[str, object]:
    """Reference vs. a regressed agent that takes more steps and over-calls one tool."""
    rng = np.random.default_rng(0)
    ref_steps = rng.integers(1, 6, size=500)
    cur_steps = rng.integers(5, 11, size=500)  # the agent now takes more steps

    ref_tools = (["retriever"] * 300) + (["calculator"] * 200) + (["web_search"] * 100)
    cur_tools = (["calculator"] * 500) + (["retriever"] * 50) + (["web_search"] * 10)

    scores = {
        "step_count": step_count_psi(ref_steps, cur_steps),
        "tool_usage": tool_usage_psi(ref_tools, cur_tools),
    }
    return evaluate_drift(scores)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Agent behavioral drift (PSI) check")
    parser.add_argument("--threshold", type=float, default=0.25)
    args = parser.parse_args(argv)

    summary = _demo()
    summary["threshold"] = args.threshold
    summary["drift_detected"] = summary["max_psi"] > args.threshold  # type: ignore[index]
    print(json.dumps(summary, indent=2))
    return 1 if summary["drift_detected"] else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
