import logging
from typing import Any, Dict
import aio_pika
import redis.asyncio as aioredis
from fastapi import APIRouter, Response, status
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from sqlalchemy import text

from config.settings import settings
from src.database.session import async_engine

logger = logging.getLogger("ai_for_salers.health")
router = APIRouter(tags=["Health & Monitoring"])


@router.get("/health", status_code=status.HTTP_200_OK)
async def liveness() -> Dict[str, str]:
    """
    Kubernetes / Docker Liveness probe.
    Returns 200 OK if FastAPI process is alive.
    """
    return {"status": "ok"}


@router.get("/ready")
async def readiness(response: Response) -> Dict[str, Any]:
    """
    Kubernetes / Docker Readiness probe.
    Verifies live connectivity to PostgreSQL, Redis, and RabbitMQ.
    """
    checks: Dict[str, str] = {
        "postgres": "down",
        "redis": "down",
        "rabbitmq": "down",
    }
    all_ok = True

    # 1. PostgreSQL check
    try:
        async with async_engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        checks["postgres"] = "up"
    except Exception as e:
        logger.warning("Readiness probe: PostgreSQL check failed: %s", str(e))
        checks["postgres"] = f"down: {str(e)}"
        all_ok = False

    # 2. Redis check
    try:
        r = aioredis.from_url(
            settings.computed_redis_url,
            socket_timeout=2.0,
            socket_connect_timeout=2.0,
        )
        await r.ping()
        await r.aclose()
        checks["redis"] = "up"
    except Exception as e:
        logger.warning("Readiness probe: Redis check failed: %s", str(e))
        checks["redis"] = f"down: {str(e)}"
        all_ok = False

    # 3. RabbitMQ check
    try:
        connection = await aio_pika.connect_robust(
            settings.computed_rabbitmq_url,
            timeout=2.0,
        )
        await connection.close()
        checks["rabbitmq"] = "up"
    except Exception as e:
        logger.warning("Readiness probe: RabbitMQ check failed: %s", str(e))
        checks["rabbitmq"] = f"down: {str(e)}"
        all_ok = False

    if not all_ok:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "degraded", "checks": checks}

    return {"status": "ready", "checks": checks}


@router.get("/metrics")
async def metrics() -> Response:
    """Prometheus metrics endpoint."""
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
