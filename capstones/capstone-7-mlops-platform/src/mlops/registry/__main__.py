"""CLI: `python -m mlops.registry <list|show|promote|current>`."""

from __future__ import annotations

import argparse
import json

from ..config import get_settings
from . import get_registry


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="mlops.registry", description="Model registry CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list", help="list all registered versions")

    p_show = sub.add_parser("show", help="show one version")
    p_show.add_argument("version", type=int)

    p_prom = sub.add_parser("promote", help="promote a version to a stage")
    p_prom.add_argument("version", type=int)
    p_prom.add_argument("--stage", default="Production", choices=["Staging", "Production", "Archived", "None"])

    p_cur = sub.add_parser("current", help="show the current version in a stage")
    p_cur.add_argument("--stage", default="Production")

    args = parser.parse_args(argv)
    reg = get_registry(get_settings())

    if args.command == "list":
        print(json.dumps([v.as_dict() for v in reg.list_versions()], indent=2))
    elif args.command == "show":
        print(json.dumps(reg.get_version(args.version).as_dict(), indent=2))
    elif args.command == "promote":
        mv = reg.promote(args.version, args.stage)
        print(json.dumps(mv.as_dict(), indent=2))
    elif args.command == "current":
        cur = reg.current(args.stage)
        print(json.dumps(cur.as_dict() if cur else None, indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
