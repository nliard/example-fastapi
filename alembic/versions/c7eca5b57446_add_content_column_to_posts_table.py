"""add content column to posts table

Revision ID: c7eca5b57446
Revises: ac5cf25c5f63
Create Date: 2023-01-16 16:03:08.099973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7eca5b57446'
down_revision = 'ac5cf25c5f63'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
