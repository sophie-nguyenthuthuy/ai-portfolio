"""CLI: `python -m mlops.serve` — run the FastAPI service with uvicorn."""

from __future__ import annotations

import argparse

from .config import get_settings


def main(argv: list[str] | None = None) -> int:
    settings = get_settings()
    parser = argparse.ArgumentParser(description="Serve the MLOps platform API")
    parser.add_argument("--host", default=settings.api_host)
    parser.add_argument("--port", type=int, default=settings.api_port)
    parser.add_argument("--reload", action="store_true", help="uvicorn autoreload (dev)")
    args = parser.parse_args(argv)

    import uvicorn

    uvicorn.run(
        "mlops.api.main:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
