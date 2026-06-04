"""Structured (JSON-ish) logging configuration."""

from __future__ import annotations

import json
import logging
import sys
from datetime import datetime, timezone

_CONFIGURED = False


class JsonFormatter(logging.Formatter):
    """Minimal JSON line formatter — no external deps."""

    def format(self, record: logging.LogRecord) -> str:
        payload = {
            "ts": datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        if record.exc_info:
            payload["exc"] = self.formatException(record.exc_info)
        for key, val in getattr(record, "extra_fields", {}).items():
            payload[key] = val
        return json.dumps(payload, ensure_ascii=False)


def get_logger(name: str = "vision", level: int | str = logging.INFO) -> logging.Logger:
    """Return a configured logger that emits one JSON object per line to stdout."""
    global _CONFIGURED
    root = logging.getLogger()
    if not _CONFIGURED:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        root.handlers.clear()
        root.addHandler(handler)
        root.setLevel(level)
        _CONFIGURED = True
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
