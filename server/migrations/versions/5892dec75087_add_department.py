"""add Department

Revision ID: 5892dec75087
Revises: 373df31f3c76
Create Date: 2025-06-15 11:01:36.898308
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '5892dec75087'
down_revision = '373df31f3c76'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'departments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('departments')