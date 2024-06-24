"""create objects

Revision ID: a12a620bd263
Revises: 1ed10756cca4
Create Date: 2024-06-09 13:06:58.458135

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a12a620bd263'
down_revision: Union[str, None] = '1ed10756cca4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name'),
    schema='app_schema'
    )
    op.create_table('region',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('code'),
    sa.UniqueConstraint('name'),
    schema='app_schema'
    )
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('region_id', sa.Integer(), nullable=False),
    sa.Column('faction_id', sa.Integer(), nullable=False),
    sa.Column('leader', sa.Boolean(), nullable=False),
    sa.Column('specialty', sa.String(), nullable=False),
    sa.Column('created', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['faction_id'], ['app_schema.faction.id'], ),
    sa.ForeignKeyConstraint(['region_id'], ['app_schema.region.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='app_schema'
    )
    op.create_table('warrior',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('code', sa.String(), nullable=False),
    sa.Column('desc', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('classification', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['house_id'], ['app_schema.house.id'], ),
    sa.PrimaryKeyConstraint('id'),
    schema='app_schema'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warrior', schema='app_schema')
    op.drop_table('house', schema='app_schema')
    op.drop_table('region', schema='app_schema')
    op.drop_table('faction', schema='app_schema')
    # ### end Alembic commands ###
