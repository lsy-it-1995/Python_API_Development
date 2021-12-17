"""add user table

Revision ID: 28bb5c798b87
Revises: 91bea399cff8
Create Date: 2021-12-15 21:01:29.234938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28bb5c798b87'
down_revision = '91bea399cff8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer, nullable = False),
                    sa.Column('email', sa.String, nullable = False),
                    sa.Column('password', sa.String, nullable = False),
                    sa.Column('create_at', sa.TIMESTAMP(timezone=True),
                            server_default=sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass

def downgrade():
    op.drop_table('users')
    pass
