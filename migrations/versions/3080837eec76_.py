"""empty message

Revision ID: 3080837eec76
Revises: dc2073687cde
Create Date: 2020-07-13 14:23:39.940573

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3080837eec76'
down_revision = 'dc2073687cde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('gti_table_row', 'bottom_hole',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'bottom_hole_plus_igti',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'company',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'degasser',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'efficiency',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'layer',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'mud_gas_quality',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('gti_table_row', 'notes',
               existing_type=mysql.VARCHAR(length=512),
               nullable=True)
    op.drop_column('gti_table_row', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gti_table_row', sa.Column('name', mysql.VARCHAR(length=128), nullable=False))
    op.alter_column('gti_table_row', 'notes',
               existing_type=mysql.VARCHAR(length=512),
               nullable=False)
    op.alter_column('gti_table_row', 'mud_gas_quality',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'layer',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'efficiency',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'degasser',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'company',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'bottom_hole_plus_igti',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('gti_table_row', 'bottom_hole',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###
