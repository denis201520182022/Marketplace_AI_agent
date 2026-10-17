import datetime
import json
import logging
import sys
from typing import Any, Dict, Optional


class JSONLogFormatter(logging.Formatter):
    """
    Structured JSON formatter designed for Grafana Loki log ingestion.
    Supports extra context attributes: service, seller_id, event_id, trace_id.
    """

    def __init__(self, service_name: str = "ai_for_salers"):
        super().__init__()
        self.service_name = service_name

    def format(self, record: logging.LogRecord) -> str:
        log_payload: Dict[str, Any] = {
            "timestamp": datetime.datetime.fromtimestamp(
                record.created, tz=datetime.timezone.utc
            ).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "service": getattr(record, "service", self.service_name),
        }

        # Context labels for Loki
        for extra_field in ("seller_id", "event_id", "trace_id", "platform", "user_id"):
            val = getattr(record, extra_field, None)
            if val is not None:
                log_payload[extra_field] = str(val)

        if record.exc_info:
            log_payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_payload, ensure_ascii=False)


def setup_logging(
    level: str = "INFO",
    service_name: str = "ai_for_salers",
) -> logging.Logger:
    """Configures root logger with JSONLogFormatter outputting to stdout."""
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    root_logger = logging.getLogger()
    root_logger.setLevel(numeric_level)

    # Remove existing handlers to avoid duplicates
    for handler in list(root_logger.handlers):
        root_logger.removeHandler(handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(numeric_level)
    stream_handler.setFormatter(JSONLogFormatter(service_name=service_name))

    root_logger.addHandler(stream_handler)
    return root_logger
