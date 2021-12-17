"""add last few columns to posts table

Revision ID: cee44ee657e4
Revises: 3293d4a2806c
Create Date: 2021-12-15 21:13:12.901639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cee44ee657e4'
down_revision = '3293d4a2806c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean, nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default=sa.text("NOW()")))


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
