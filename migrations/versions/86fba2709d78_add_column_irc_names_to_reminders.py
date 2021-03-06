"""Add column irc_name to reminders

Revision ID: 86fba2709d78
Revises: 1cb55d4fff97
Create Date: 2019-02-07 18:27:29.401466

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "86fba2709d78"
down_revision = "1cb55d4fff97"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("reminders", sa.Column("irc_name", sa.String(), nullable=True))


def downgrade():
    with op.batch_alter_table("reminders") as bop:
        bop.drop_column("irc_name")
