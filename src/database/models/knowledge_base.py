import datetime
import uuid
from typing import Any, Dict
from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class KnowledgeBaseDoc(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "knowledge_base_docs"

    seller_account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("seller_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        doc="txt | pdf | docx | xlsx",
    )
    parsed_content: Mapped[str] = mapped_column(Text, nullable=False)
    metadata_json: Mapped[Dict[str, Any]] = mapped_column(
        JSONB,
        default=dict,
        nullable=False,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    seller_account: Mapped["SellerAccount"] = relationship(
        "SellerAccount", back_populates="knowledge_base_docs"
    )
