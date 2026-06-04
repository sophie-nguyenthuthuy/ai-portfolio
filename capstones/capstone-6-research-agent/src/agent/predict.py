"""CLI entry point: ask the research agent a question from the terminal.

    python -m agent.predict --question "What is RAG and why cite sources?"

Defaults to the fully-offline FakeLLM + SimpleGraph + FakeSearch backends.
"""

from __future__ import annotations

import argparse
import json

from .config import get_settings
from .pipeline import run


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the research agent on a question.")
    parser.add_argument(
        "--question",
        "-q",
        default="What is an AI agent and when does it stop?",
        help="the research question",
    )
    parser.add_argument("--max-steps", type=int, default=None, help="override step budget")
    args = parser.parse_args(argv)

    settings = get_settings()
    if args.max_steps is not None:
        settings = settings.model_copy(update={"max_steps": args.max_steps})

    result = run(args.question, settings=settings)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
