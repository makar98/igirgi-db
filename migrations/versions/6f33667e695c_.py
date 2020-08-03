"""empty message

Revision ID: 6f33667e695c
Revises: 52666d6bdb2f
Create Date: 2020-06-16 13:11:05.466603

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6f33667e695c'
down_revision = '52666d6bdb2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quality_sheet', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('field_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('pad_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('well_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('well_type_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('wellbore_id', sa.Integer(), nullable=False))
    op.add_column('quality_sheet', sa.Column('wellbore_type_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'quality_sheet', 'well', ['well_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'field', ['field_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'customer', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'well_type', ['well_type_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'pad', ['pad_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'wellbore_type', ['wellbore_type_id'], ['id'])
    op.create_foreign_key(None, 'quality_sheet', 'wellbore', ['wellbore_id'], ['id'])
    op.drop_column('quality_sheet', 'well_section')
    op.drop_column('quality_sheet', 'field')
    op.drop_column('quality_sheet', 'customer')
    op.drop_column('quality_sheet', 'pad_num')
    op.drop_column('quality_sheet', 'well_num')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quality_sheet', sa.Column('well_num', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('quality_sheet', sa.Column('pad_num', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('quality_sheet', sa.Column('customer', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('quality_sheet', sa.Column('field', mysql.VARCHAR(length=128), nullable=True))
    op.add_column('quality_sheet', sa.Column('well_section', mysql.VARCHAR(length=128), nullable=True))
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_constraint(None, 'quality_sheet', type_='foreignkey')
    op.drop_column('quality_sheet', 'wellbore_type_id')
    op.drop_column('quality_sheet', 'wellbore_id')
    op.drop_column('quality_sheet', 'well_type_id')
    op.drop_column('quality_sheet', 'well_id')
    op.drop_column('quality_sheet', 'pad_id')
    op.drop_column('quality_sheet', 'field_id')
    op.drop_column('quality_sheet', 'customer_id')
    # ### end Alembic commands ###
