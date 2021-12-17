"""add foreign-key to posts table

Revision ID: 3293d4a2806c
Revises: 28bb5c798b87
Create Date: 2021-12-15 21:08:38.306123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3293d4a2806c'
down_revision = '28bb5c798b87'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer, nullable = False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users",
                            local_cols = ['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
