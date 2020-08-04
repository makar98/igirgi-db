"""empty message

Revision ID: 735cbec3c99d
Revises: d97db56727cc
Create Date: 2020-04-15 11:31:37.438786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '735cbec3c99d'
down_revision = 'd97db56727cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wellbore',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('change_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('well_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['well_id'], ['well.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wellbore')
    # ### end Alembic commands ###