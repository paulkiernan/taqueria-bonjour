"""Renames user table, adds deleted and delivery_errors fields

Revision ID: b72abb39d5c2
Revises: fae6e83c76ea
Create Date: 2020-12-23 21:56:22.637639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b72abb39d5c2"
down_revision = "fae6e83c76ea"
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.drop_index("ix_user__phone_number")
        batch_op.drop_index("ix_user_name")

    op.rename_table("user", "users")

    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("delivery_errors", sa.Integer(), nullable=True)
        )
        batch_op.add_column(sa.Column("deleted", sa.Boolean(), nullable=True))
        batch_op.create_index(
            batch_op.f("ix_users__phone_number"),
            ["_phone_number"],
            unique=True,
        )
        batch_op.create_index(
            batch_op.f("ix_users_name"), ["name"], unique=True
        )


def downgrade():

    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_users_name"))
        batch_op.drop_index(batch_op.f("ix_users__phone_number"))

        batch_op.drop_column("delivery_errors")
        batch_op.drop_column("deleted")

    op.rename_table("users", "user")

    with op.batch_alter_table("user", schema=None) as batch_op:
        batch_op.create_index("ix_user_name", ["name"], unique=1)
        batch_op.create_index(
            "ix_user__phone_number", ["_phone_number"], unique=1
        )
