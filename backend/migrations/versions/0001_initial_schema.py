"""Initial schema: sessions, messages, activity.

Revision ID: 0001_initial
Revises:
Create Date: 2026-10-21
"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

JSONType = sa.JSON().with_variant(JSONB(), "postgresql")
STATUS_CHECK = ("(role = 'user' AND status IS NULL) OR (role = 'assistant' AND status IN "
                "('answered', 'partial', 'not_documented', 'conflicting_sources', 'no_evidence', 'error'))")


def upgrade() -> None:
    op.create_table(
        "sessions",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("title", sa.String(200), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_sessions_updated_at", "sessions", ["updated_at"])

    op.create_table(
        "messages",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("session_id", sa.Uuid(), sa.ForeignKey("sessions.id", ondelete="CASCADE"), nullable=False),
        sa.Column("seq", sa.Integer(), nullable=False),
        sa.Column("role", sa.String(16), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("status", sa.String(32), nullable=True),
        sa.Column("citations", JSONType, nullable=True),
        sa.Column("details", JSONType, nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.UniqueConstraint("session_id", "seq", name="uq_messages_session_seq"),
        sa.CheckConstraint("role IN ('user', 'assistant')", name="ck_messages_role"),
        sa.CheckConstraint(STATUS_CHECK, name="ck_messages_status"),
        sa.CheckConstraint("seq >= 1", name="ck_messages_seq_positive"),
    )
    op.create_index("ix_messages_session_seq", "messages", ["session_id", "seq"])

    op.create_table(
        "activity",
        sa.Column("id", sa.Uuid(), primary_key=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.Column("session_id", sa.Uuid(), sa.ForeignKey("sessions.id", ondelete="SET NULL"), nullable=True),
        sa.Column("event", sa.String(40), nullable=False),
        sa.Column("status", sa.String(32), nullable=False),
        sa.Column("http_status", sa.Integer(), nullable=False),
        sa.Column("duration_ms", sa.Integer(), nullable=False),
        sa.Column("evidence_count", sa.Integer(), nullable=True),
        sa.Column("citation_count", sa.Integer(), nullable=True),
        sa.Column("model", sa.String(80), nullable=True),
        sa.Column("error_kind", sa.String(40), nullable=True),
    )
    op.create_index("ix_activity_created_at", "activity", ["created_at"])


def downgrade() -> None:
    op.drop_index("ix_activity_created_at", table_name="activity")
    op.drop_table("activity")
    op.drop_index("ix_messages_session_seq", table_name="messages")
    op.drop_table("messages")
    op.drop_index("ix_sessions_updated_at", table_name="sessions")
    op.drop_table("sessions")
