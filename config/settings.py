import json
from typing import Any, List, Optional, Union
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # General
    PROJECT_NAME: str = "AI for Salers"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"

    # API Server
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    # PostgreSQL
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ai_for_salers"
    DATABASE_URL: Optional[str] = None

    @property
    def async_database_url(self) -> str:
        if self.DATABASE_URL:
            if self.DATABASE_URL.startswith("postgresql://"):
                return self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
            return self.DATABASE_URL
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None
    REDIS_URL: Optional[str] = None

    @property
    def computed_redis_url(self) -> str:
        if self.REDIS_URL:
            return self.REDIS_URL
        auth = f":{self.REDIS_PASSWORD}@" if self.REDIS_PASSWORD else ""
        return f"redis://{auth}{self.REDIS_HOST}:{self.REDIS_PORT}/0"

    # RabbitMQ
    RABBITMQ_HOST: str = "localhost"
    RABBITMQ_PORT: int = 5672
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASSWORD: str = "guest"
    RABBITMQ_URL: Optional[str] = None

    @property
    def computed_rabbitmq_url(self) -> str:
        if self.RABBITMQ_URL:
            return self.RABBITMQ_URL
        return (
            f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@"
            f"{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}/"
        )

    # Qdrant
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333

    # Cryptography (AES-256 Master Key)
    # 32 bytes hex or urlsafe-base64 or 32 raw chars
    SECRET_KEY_ENCRYPTION: str = Field(
        default="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        description="Master key for AES-256-GCM encryption of credentials",
    )

    # Proxy & Network (Hybrid & Sovereign Modes)
    USE_PROXY: bool = False
    PROXY_URL: Optional[str] = None

    # Bots Configuration
    TELEGRAM_BOT_TOKEN: str = ""
    MAX_BOT_TOKEN: str = ""
    ADMIN_TELEGRAM_IDS: Any = Field(default_factory=list)
    ADMIN_MAX_IDS: Any = Field(default_factory=list)

    @field_validator("ADMIN_TELEGRAM_IDS", mode="before")
    @classmethod
    def parse_admin_telegram_ids(cls, v) -> List[int]:
        if isinstance(v, (int, float)):
            return [int(v)]
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return []
            if v.startswith("["):
                try:
                    return [int(x) for x in json.loads(v)]
                except Exception:
                    pass
            return [int(x.strip()) for x in v.split(",") if x.strip()]
        if isinstance(v, (list, tuple, set)):
            return [int(x) for x in v]
        return []

    @field_validator("ADMIN_MAX_IDS", mode="before")
    @classmethod
    def parse_admin_max_ids(cls, v) -> List[str]:
        if isinstance(v, (int, float)):
            return [str(v)]
        if isinstance(v, str):
            v = v.strip()
            if not v:
                return []
            if v.startswith("["):
                try:
                    return [str(x) for x in json.loads(v)]
                except Exception:
                    pass
            return [x.strip() for x in v.split(",") if x.strip()]
        if isinstance(v, (list, tuple, set)):
            return [str(x) for x in v]
        return []

    # LLM Settings
    OPENAI_API_KEY: str = ""
    OPENAI_BASE_URL: Optional[str] = None
    OPENAI_MODEL: str = "gpt-4o-mini"

    # Langfuse — Self-Hosted (локальный сервер, порт 3002)
    # Облачный Langfuse Cloud НЕ используется — все данные хранятся локально.
    LANGFUSE_PUBLIC_KEY: str = "lf-pk-local-change-me"
    LANGFUSE_SECRET_KEY: str = "lf-sk-local-change-me"
    LANGFUSE_HOST: str = "http://localhost:3002"

    # YooKassa
    YOOKASSA_SHOP_ID: str = ""
    YOOKASSA_SECRET_KEY: str = ""


settings = Settings()
