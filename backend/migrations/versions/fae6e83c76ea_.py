"""Inital DB Schema commit

Revision ID: fae6e83c76ea
Revises:
Create Date: 2020-12-18 22:28:46.321814

"""
from alembic import op
import sqlalchemy as sa


revision = "fae6e83c76ea"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.Unicode(length=255), nullable=True),
        sa.Column("_phone_number", sa.Unicode(length=20), nullable=True),
        sa.Column("country_code", sa.Unicode(length=8), nullable=True),
        sa.Column("sends", sa.Integer(), nullable=True),
        sa.Column("responses", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_user__phone_number"), "user", ["_phone_number"], unique=True
    )
    op.create_index(op.f("ix_user_name"), "user", ["name"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_user_name"), table_name="user")
    op.drop_index(op.f("ix_user__phone_number"), table_name="user")
    op.drop_table("user")
