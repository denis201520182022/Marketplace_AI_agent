import datetime
from decimal import Decimal
import uuid
from typing import List, Optional
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class ReviewQuestion(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "reviews_questions"

    seller_account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("seller_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    external_id: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        index=True,
        doc="Marketplace review or question ID",
    )
    event_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        doc="review | question",
    )
    rating: Mapped[Optional[int]] = mapped_column(
        Integer,
        nullable=True,
        doc="1..5 for reviews, null for questions",
    )
    product_article: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        index=True,
        doc="nmId for WB, SKU for Ozon",
    )
    product_title: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    user_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    pros: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    cons: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    ai_draft_answer: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    final_answer: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(
        String(64),
        default="pending",
        nullable=False,
        index=True,
        doc=(
            "pending | processing | waiting_approval | published | "
            "rejected | ignored_out_of_scope | out_of_quota | "
            "resolved_externally | error"
        ),
    )
    idempotency_key: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
        index=True,
    )
    notification_message_id: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        doc="Message ID in Telegram/MAX to edit during approval",
    )
    handled_by_user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    handled_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    published_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relationships
    seller_account: Mapped["SellerAccount"] = relationship(
        "SellerAccount", back_populates="reviews_questions"
    )
    audit_logs: Mapped[List["EventAuditLog"]] = relationship(
        "EventAuditLog", back_populates="review_question", cascade="all, delete-orphan"
    )


class EventAuditLog(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "event_audit_log"

    event_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("reviews_questions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    model_name: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        doc="gpt-4o-mini | gigachat | etc",
    )
    prompt_tokens: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    completion_tokens: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    latency_ms: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False, doc="Inference latency in ms"
    )
    estimated_cost: Mapped[Decimal] = mapped_column(
        Numeric(10, 4), default=Decimal("0.0000"), nullable=False, doc="Cost in RUB"
    )
    langfuse_trace_id: Mapped[Optional[str]] = mapped_column(
        String(128), nullable=True, index=True
    )

    # Relationships
    review_question: Mapped["ReviewQuestion"] = relationship(
        "ReviewQuestion", back_populates="audit_logs"
    )
