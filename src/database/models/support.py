import datetime
import uuid
from typing import Any, Dict, List, Optional
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class SupportTicket(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "support_tickets"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    ticket_number: Mapped[int] = mapped_column(
        Integer,
        Identity(start=1001, cycle=False),
        nullable=False,
        unique=True,
        index=True,
        doc="Human-friendly ticket number starting at 1001",
    )
    status: Mapped[str] = mapped_column(
        String(32),
        default="open",
        nullable=False,
        index=True,
        doc="open | in_progress | resolved",
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="support_tickets")
    messages: Mapped[List["SupportMessage"]] = relationship(
        "SupportMessage", back_populates="ticket", cascade="all, delete-orphan"
    )


class SupportMessage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "support_messages"

    ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("support_tickets.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    sender_type: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        doc="user | admin",
    )
    platform: Mapped[str] = mapped_column(
        String(32),
        default="telegram",
        nullable=False,
        doc="telegram | max",
    )
    admin_message_id: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        doc="Telegram/MAX message ID in admin chat for reply routing",
    )
    user_message_id: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        doc="Telegram/MAX message ID in user chat",
    )
    message_text: Mapped[str] = mapped_column(Text, nullable=False)
    attachments: Mapped[List[Dict[str, Any]]] = mapped_column(
        JSONB,
        default=list,
        nullable=False,
    )

    # Relationships
    ticket: Mapped["SupportTicket"] = relationship("SupportTicket", back_populates="messages")
