import uuid
from typing import List, Optional
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class User(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "users"

    telegram_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        unique=True,
        index=True,
        nullable=True,
        doc="Telegram user ID (bigint)",
    )
    max_id: Mapped[Optional[str]] = mapped_column(
        String(128),
        unique=True,
        index=True,
        nullable=True,
        doc="MAX user GUID (string)",
    )
    username: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    role: Mapped[str] = mapped_column(
        String(32),
        default="seller",
        nullable=False,
        doc="Role: seller | admin",
    )

    # Relationships
    seller_accounts: Mapped[List["SellerAccount"]] = relationship(
        "SellerAccount", back_populates="user", cascade="all, delete-orphan"
    )
    subscriptions: Mapped[List["Subscription"]] = relationship(
        "Subscription", back_populates="user", cascade="all, delete-orphan"
    )
    payments: Mapped[List["Payment"]] = relationship(
        "Payment", back_populates="user", cascade="all, delete-orphan"
    )
    store_memberships: Mapped[List["StoreMembers"]] = relationship(
        "StoreMembers", back_populates="user"
    )
    support_tickets: Mapped[List["SupportTicket"]] = relationship(
        "SupportTicket", back_populates="user", cascade="all, delete-orphan"
    )
