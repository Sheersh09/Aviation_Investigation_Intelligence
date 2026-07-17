import json
import logging
from datetime import datetime, timezone
from logging.config import dictConfig
from typing import Any

# Phase 1 change: emit JSON log records so later ingestion and retrieval events are easy to filter and correlate.


class JsonFormatter(logging.Formatter):
    """Format standard logging records as one JSON object per line."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, Any] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }
        if record.exc_info:
            payload["exception"] = self.formatException(record.exc_info)
        return json.dumps(payload, ensure_ascii=False)


def configure_logging(log_level: str, log_format: str = "json") -> None:
    formatter_name = "json" if log_format.lower() == "json" else "standard"
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "json": {"()": "app.core.logging.JsonFormatter"},
                "standard": {
                    "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
                },
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": formatter_name,
                    "stream": "ext://sys.stdout",
                }
            },
            "root": {"level": log_level.upper(), "handlers": ["console"]},
        }
    )
