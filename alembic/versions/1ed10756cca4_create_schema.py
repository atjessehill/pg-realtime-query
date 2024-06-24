"""create schema

Revision ID: 1ed10756cca4
Revises: 
Create Date: 2024-06-09 12:28:41.231193

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ed10756cca4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create new schema
    op.execute("CREATE SCHEMA IF NOT EXISTS app_schema")

def downgrade():
    # Drop schema if rolling back
    op.execute("DROP SCHEMA app_schema")
