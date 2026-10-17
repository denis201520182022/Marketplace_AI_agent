import datetime
import uuid
from typing import List, Optional
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    String,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class SellerAccount(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "seller_accounts"

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    marketplace: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        doc="wb | ozon | avito | yandex_market | mock",
    )
    account_name: Mapped[str] = mapped_column(String(255), nullable=False)
    encrypted_credentials: Mapped[str] = mapped_column(
        Text,
        nullable=False,
        doc="AES-256-GCM encrypted credentials JSON",
    )
    mode: Mapped[str] = mapped_column(
        String(32),
        default="confirm_all",
        nullable=False,
        doc="auto | confirm_all",
    )
    scope_mode: Mapped[str] = mapped_column(
        String(32),
        default="all",
        nullable=False,
        doc="all | whitelist | blacklist",
    )
    notification_platform: Mapped[str] = mapped_column(
        String(32),
        default="telegram",
        nullable=False,
        doc="telegram | max",
    )
    notification_target_type: Mapped[str] = mapped_column(
        String(32),
        default="user",
        nullable=False,
        doc="user | group_chat",
    )
    notification_target_id: Mapped[Optional[str]] = mapped_column(
        String(128),
        nullable=True,
        doc="ID of recipient user or group chat",
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    last_polled_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="seller_accounts")
    members: Mapped[List["StoreMembers"]] = relationship(
        "StoreMembers", back_populates="seller_account", cascade="all, delete-orphan"
    )
    product_scopes: Mapped[List["StoreProductsScope"]] = relationship(
        "StoreProductsScope", back_populates="seller_account", cascade="all, delete-orphan"
    )
    knowledge_base_docs: Mapped[List["KnowledgeBaseDoc"]] = relationship(
        "KnowledgeBaseDoc", back_populates="seller_account", cascade="all, delete-orphan"
    )
    reviews_questions: Mapped[List["ReviewQuestion"]] = relationship(
        "ReviewQuestion", back_populates="seller_account", cascade="all, delete-orphan"
    )


class StoreMembers(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "store_members"

    seller_account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("seller_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    user_id: Mapped[Optional[uuid.UUID]] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
    )
    invite_token: Mapped[str] = mapped_column(
        String(128),
        unique=True,
        nullable=False,
        index=True,
    )
    status: Mapped[str] = mapped_column(
        String(32),
        default="pending",
        nullable=False,
        doc="pending | accepted | revoked",
    )
    role: Mapped[str] = mapped_column(
        String(32),
        default="manager",
        nullable=False,
        doc="owner | manager",
    )
    invited_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    expires_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )
    accepted_at: Mapped[Optional[datetime.datetime]] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    # Relationships
    seller_account: Mapped["SellerAccount"] = relationship(
        "SellerAccount", back_populates="members"
    )
    user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="store_memberships"
    )


class StoreProductsScope(Base, UUIDPrimaryKeyMixin):
    __tablename__ = "store_products_scope"
    __table_args__ = (
        UniqueConstraint("seller_account_id", "product_article", name="uq_seller_product_article"),
    )

    seller_account_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("seller_accounts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    product_article: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        doc="nmId for WB or SKU for Ozon",
    )
    product_title: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    added_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    # Relationships
    seller_account: Mapped["SellerAccount"] = relationship(
        "SellerAccount", back_populates="product_scopes"
    )
