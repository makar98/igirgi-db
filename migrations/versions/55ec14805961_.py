"""empty message

Revision ID: 55ec14805961
Revises: 19413d27b2db
Create Date: 2020-04-13 15:26:56.642449

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '55ec14805961'
down_revision = '19413d27b2db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('layer', 'field_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.drop_index('customer_id', table_name='layer')
    op.create_foreign_key(None, 'layer', 'field', ['field_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'layer', type_='foreignkey')
    op.create_index('customer_id', 'layer', ['field_id'], unique=False)
    op.alter_column('layer', 'field_id',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    # ### end Alembic commands ###
