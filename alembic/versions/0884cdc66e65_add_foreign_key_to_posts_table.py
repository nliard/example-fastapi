"""add foreign-key to posts table

Revision ID: 0884cdc66e65
Revises: 12c2efecc291
Create Date: 2023-01-16 16:30:13.466535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0884cdc66e65'
down_revision = '12c2efecc291'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
