"""empty message

Revision ID: 7c201a7b9e4d
Revises: 
Create Date: 2024-03-11 18:29:31.734825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c201a7b9e4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('properties',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('numBedrooms', sa.Integer(), nullable=True),
    sa.Column('numBathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=128), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('propertyType', sa.String(length=20), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('photo', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('properties')
    # ### end Alembic commands ###
