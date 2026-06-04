"""Text data-drift detection via Population Stability Index (PSI).

Compares a reference corpus against a current corpus along two axes:
  * review length distribution (chars), bucketed into quantile bins, and
  * vocabulary distribution (relative frequency of the most common reference
    tokens, with an out-of-vocabulary catch-all bucket).

PSI interpretation (industry rule of thumb):
  < 0.1  no significant drift
  0.1-0.25 moderate drift
  > 0.25 significant drift
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass, field

import numpy as np

_EPS = 1e-6
_TOKEN_RE = re.compile(r"\w+", re.UNICODE)


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower())


def _psi_from_counts(ref: np.ndarray, cur: np.ndarray) -> float:
    ref_pct = ref / max(ref.sum(), _EPS)
    cur_pct = cur / max(cur.sum(), _EPS)
    ref_pct = np.clip(ref_pct, _EPS, None)
    cur_pct = np.clip(cur_pct, _EPS, None)
    return float(np.sum((cur_pct - ref_pct) * np.log(cur_pct / ref_pct)))


def length_psi(reference: list[str], current: list[str], bins: int = 10) -> float:
    """PSI over the character-length distribution of the two corpora."""
    ref_len = np.array([len(t) for t in reference], dtype=float)
    cur_len = np.array([len(t) for t in current], dtype=float)
    if ref_len.size == 0 or cur_len.size == 0:
        return 0.0
    quantiles = np.quantile(ref_len, np.linspace(0, 1, bins + 1))
    edges = np.unique(quantiles)
    if edges.size < 2:
        edges = np.array([ref_len.min() - 1, ref_len.max() + 1])
    ref_hist, _ = np.histogram(ref_len, bins=edges)
    cur_hist, _ = np.histogram(cur_len, bins=edges)
    return _psi_from_counts(ref_hist.astype(float), cur_hist.astype(float))


def vocab_psi(reference: list[str], current: list[str], top_k: int = 50) -> float:
    """PSI over the top-k reference vocabulary plus an OOV bucket."""
    ref_tokens = [tok for text in reference for tok in _tokenize(text)]
    cur_tokens = [tok for text in current for tok in _tokenize(text)]
    if not ref_tokens or not cur_tokens:
        return 0.0
    ref_counter = Counter(ref_tokens)
    vocab = [tok for tok, _ in ref_counter.most_common(top_k)]
    vocab_set = set(vocab)
    cur_counter = Counter(cur_tokens)

    ref_vec = np.array([ref_counter[t] for t in vocab] + [0.0], dtype=float)
    cur_vec = np.array([cur_counter[t] for t in vocab], dtype=float)
    cur_oov = sum(c for t, c in cur_counter.items() if t not in vocab_set)
    ref_oov = sum(c for t, c in ref_counter.items() if t not in vocab_set)
    ref_vec[-1] = ref_oov
    cur_vec = np.append(cur_vec, cur_oov)
    return _psi_from_counts(ref_vec, cur_vec)


@dataclass
class DriftReport:
    length_psi: float
    vocab_psi: float
    threshold: float = 0.25
    drifted: bool = field(init=False)

    def __post_init__(self) -> None:
        self.drifted = (self.length_psi > self.threshold) or (
            self.vocab_psi > self.threshold
        )

    def to_dict(self) -> dict:
        return {
            "length_psi": round(self.length_psi, 6),
            "vocab_psi": round(self.vocab_psi, 6),
            "threshold": self.threshold,
            "drifted": self.drifted,
        }


def detect_drift(
    reference: list[str],
    current: list[str],
    *,
    threshold: float = 0.25,
) -> DriftReport:
    """Compute length + vocabulary PSI and flag drift against ``threshold``."""
    return DriftReport(
        length_psi=length_psi(reference, current),
        vocab_psi=vocab_psi(reference, current),
        threshold=threshold,
    )


def _read_texts(path: str) -> list[str]:
    import pandas as pd

    df = pd.read_csv(path)
    col = "text" if "text" in df.columns else df.columns[0]
    return df[col].astype(str).tolist()


def main(argv: list[str] | None = None) -> int:  # pragma: no cover - CLI glue
    parser = argparse.ArgumentParser(description="Text drift (PSI) check")
    parser.add_argument("--reference", required=True, help="reference CSV with text column")
    parser.add_argument("--current", required=True, help="current CSV with text column")
    parser.add_argument("--threshold", type=float, default=0.25)
    args = parser.parse_args(argv)
    report = detect_drift(
        _read_texts(args.reference),
        _read_texts(args.current),
        threshold=args.threshold,
    )
    print(json.dumps(report.to_dict(), ensure_ascii=False, indent=2))
    return 1 if report.drifted else 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
