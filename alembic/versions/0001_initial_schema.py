"""0001_initial_schema

Revision ID: 0001_initial_schema
Revises: 
Create Date: 2026-10-17 21:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '0001_initial_schema'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. users
    op.create_table(
        'users',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('telegram_id', sa.BigInteger(), nullable=True),
        sa.Column('max_id', sa.String(length=128), nullable=True),
        sa.Column('username', sa.String(length=255), nullable=True),
        sa.Column('role', sa.String(length=32), nullable=False, server_default='seller'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_users_telegram_id', 'users', ['telegram_id'], unique=True)
    op.create_index('ix_users_max_id', 'users', ['max_id'], unique=True)

    # 2. seller_accounts
    op.create_table(
        'seller_accounts',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('marketplace', sa.String(length=32), nullable=False),
        sa.Column('account_name', sa.String(length=255), nullable=False),
        sa.Column('encrypted_credentials', sa.Text(), nullable=False),
        sa.Column('mode', sa.String(length=32), nullable=False, server_default='confirm_all'),
        sa.Column('scope_mode', sa.String(length=32), nullable=False, server_default='all'),
        sa.Column('notification_platform', sa.String(length=32), nullable=False, server_default='telegram'),
        sa.Column('notification_target_type', sa.String(length=32), nullable=False, server_default='user'),
        sa.Column('notification_target_id', sa.String(length=128), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
        sa.Column('last_polled_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_seller_accounts_user_id', 'seller_accounts', ['user_id'])

    # 3. store_members
    op.create_table(
        'store_members',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('seller_account_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('seller_accounts.id', ondelete='CASCADE'), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('invite_token', sa.String(length=128), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='pending'),
        sa.Column('role', sa.String(length=32), nullable=False, server_default='manager'),
        sa.Column('invited_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('accepted_at', sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index('ix_store_members_seller_account_id', 'store_members', ['seller_account_id'])
    op.create_index('ix_store_members_user_id', 'store_members', ['user_id'])
    op.create_index('ix_store_members_invite_token', 'store_members', ['invite_token'], unique=True)

    # 4. store_products_scope
    op.create_table(
        'store_products_scope',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('seller_account_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('seller_accounts.id', ondelete='CASCADE'), nullable=False),
        sa.Column('product_article', sa.String(length=128), nullable=False),
        sa.Column('product_title', sa.String(length=512), nullable=True),
        sa.Column('added_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.UniqueConstraint('seller_account_id', 'product_article', name='uq_seller_product_article')
    )
    op.create_index('ix_store_products_scope_seller_account_id', 'store_products_scope', ['seller_account_id'])

    # 5. knowledge_base_docs
    op.create_table(
        'knowledge_base_docs',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('seller_account_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('seller_accounts.id', ondelete='CASCADE'), nullable=False),
        sa.Column('filename', sa.String(length=255), nullable=False),
        sa.Column('file_type', sa.String(length=32), nullable=False),
        sa.Column('parsed_content', sa.Text(), nullable=False),
        sa.Column('metadata_json', postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default='{}'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_knowledge_base_docs_seller_account_id', 'knowledge_base_docs', ['seller_account_id'])

    # 6. reviews_questions
    op.create_table(
        'reviews_questions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('seller_account_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('seller_accounts.id', ondelete='CASCADE'), nullable=False),
        sa.Column('external_id', sa.String(length=128), nullable=False),
        sa.Column('event_type', sa.String(length=32), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=True),
        sa.Column('product_article', sa.String(length=128), nullable=False),
        sa.Column('product_title', sa.Text(), nullable=True),
        sa.Column('user_text', sa.Text(), nullable=True),
        sa.Column('pros', sa.Text(), nullable=True),
        sa.Column('cons', sa.Text(), nullable=True),
        sa.Column('ai_draft_answer', sa.Text(), nullable=True),
        sa.Column('final_answer', sa.Text(), nullable=True),
        sa.Column('status', sa.String(length=64), nullable=False, server_default='pending'),
        sa.Column('idempotency_key', sa.String(length=255), nullable=False),
        sa.Column('notification_message_id', sa.String(length=128), nullable=True),
        sa.Column('handled_by_user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='SET NULL'), nullable=True),
        sa.Column('handled_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('published_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_reviews_questions_seller_account_id', 'reviews_questions', ['seller_account_id'])
    op.create_index('ix_reviews_questions_external_id', 'reviews_questions', ['external_id'])
    op.create_index('ix_reviews_questions_product_article', 'reviews_questions', ['product_article'])
    op.create_index('ix_reviews_questions_status', 'reviews_questions', ['status'])
    op.create_index('ix_reviews_questions_idempotency_key', 'reviews_questions', ['idempotency_key'], unique=True)

    # 7. event_audit_log
    op.create_table(
        'event_audit_log',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('event_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('reviews_questions.id', ondelete='CASCADE'), nullable=False),
        sa.Column('model_name', sa.String(length=64), nullable=False),
        sa.Column('prompt_tokens', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('completion_tokens', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('latency_ms', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('estimated_cost', sa.Numeric(precision=10, scale=4), nullable=False, server_default='0.0000'),
        sa.Column('langfuse_trace_id', sa.String(length=128), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_event_audit_log_event_id', 'event_audit_log', ['event_id'])
    op.create_index('ix_event_audit_log_langfuse_trace_id', 'event_audit_log', ['langfuse_trace_id'])

    # 8. subscriptions
    op.create_table(
        'subscriptions',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('plan_code', sa.String(length=32), nullable=False),
        sa.Column('responses_limit', sa.Integer(), nullable=False),
        sa.Column('responses_used', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('starts_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('expires_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.text('true')),
    )
    op.create_index('ix_subscriptions_user_id', 'subscriptions', ['user_id'])

    # 9. payments
    op.create_table(
        'payments',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('yookassa_payment_id', sa.String(length=128), nullable=False),
        sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('currency', sa.String(length=8), nullable=False, server_default='RUB'),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='pending'),
        sa.Column('payment_type', sa.String(length=32), nullable=False),
        sa.Column('payment_metadata', postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default='{}'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_payments_user_id', 'payments', ['user_id'])
    op.create_index('ix_payments_yookassa_payment_id', 'payments', ['yookassa_payment_id'], unique=True)

    # 10. support_tickets
    op.create_table(
        'support_tickets',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('ticket_number', sa.Integer(), sa.Identity(start=1001, cycle=False), nullable=False),
        sa.Column('status', sa.String(length=32), nullable=False, server_default='open'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_support_tickets_user_id', 'support_tickets', ['user_id'])
    op.create_index('ix_support_tickets_ticket_number', 'support_tickets', ['ticket_number'], unique=True)
    op.create_index('ix_support_tickets_status', 'support_tickets', ['status'])

    # 11. support_messages
    op.create_table(
        'support_messages',
        sa.Column('id', postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column('ticket_id', postgresql.UUID(as_uuid=True), sa.ForeignKey('support_tickets.id', ondelete='CASCADE'), nullable=False),
        sa.Column('sender_type', sa.String(length=32), nullable=False),
        sa.Column('platform', sa.String(length=32), nullable=False, server_default='telegram'),
        sa.Column('admin_message_id', sa.String(length=128), nullable=True),
        sa.Column('user_message_id', sa.String(length=128), nullable=True),
        sa.Column('message_text', sa.Text(), nullable=False),
        sa.Column('attachments', postgresql.JSONB(astext_type=sa.Text()), nullable=False, server_default='[]'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    )
    op.create_index('ix_support_messages_ticket_id', 'support_messages', ['ticket_id'])


def downgrade() -> None:
    op.drop_table('support_messages')
    op.drop_table('support_tickets')
    op.drop_table('payments')
    op.drop_table('subscriptions')
    op.drop_table('event_audit_log')
    op.drop_table('reviews_questions')
    op.drop_table('knowledge_base_docs')
    op.drop_table('store_products_scope')
    op.drop_table('store_members')
    op.drop_table('seller_accounts')
    op.drop_table('users')
