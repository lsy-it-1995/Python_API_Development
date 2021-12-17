"""add content column to posts table

Revision ID: 91bea399cff8
Revises: 34d3b4cedbc1
Create Date: 2021-12-15 20:57:59.292523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91bea399cff8'
down_revision = '34d3b4cedbc1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))


def downgrade():
    op.drop_column('posts','content')