import asyncio
from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.logging import setup_logging
from config.settings import settings
from src.api.routers.health import router as health_router
from src.database.session import async_engine

# Initialize JSON logging for Loki
setup_logging(level=settings.LOG_LEVEL, service_name="fastapi_core")
logger = logging.getLogger("ai_for_salers.main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    Performs startup checks, database pool verification, and graceful shutdown.
    """
    logger.info("Starting up AI for Salers backend...", extra={"service": "core"})
    
    # Warm up / verify database pool
    try:
        async with asyncio.timeout(2.0):
            async with async_engine.connect() as conn:
                logger.info("Database connection established successfully.")
    except Exception as e:
        logger.warning(
            "Database connection failed at startup (service will retry on readiness check): %s",
            str(e),
        )

    yield

    # Graceful shutdown
    logger.info("Shutting down AI for Salers backend...", extra={"service": "core"})
    await async_engine.dispose()
    logger.info("Database engine disposed.")


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Омниканальный AI-агент для автоматизации поддержки селлеров Wildberries и Ozon",
    version="0.1.0",
    lifespan=lifespan,
    docs_url="/docs" if settings.DEBUG else None,
    redoc_url="/redoc" if settings.DEBUG else None,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
    )
