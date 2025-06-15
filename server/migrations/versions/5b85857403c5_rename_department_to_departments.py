"""rename department to departments

Revision ID: 5b85857403c5
Revises: 2f3ee5b97d25
Create Date: 2025-06-15 12:56:35.041234
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = '5b85857403c5'
down_revision = '2f3ee5b97d25'
branch_labels = None
depends_on = None

def upgrade():
    op.rename_table('department', 'departments')

def downgrade():
    op.rename_table('departments', 'department')
