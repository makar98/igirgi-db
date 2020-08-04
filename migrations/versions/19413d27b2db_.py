"""empty message

Revision ID: 19413d27b2db
Revises: 2841ec9efd7c
Create Date: 2020-04-13 15:15:13.976153

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '19413d27b2db'
down_revision = '2841ec9efd7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layer', sa.Column('field_id', sa.Integer(), nullable=False))
    op.drop_constraint('layer_ibfk_1', 'layer', type_='foreignkey')
    op.create_foreign_key(None, 'layer', 'field', ['field_id'], ['id'])
    op.drop_column('layer', 'customer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layer', sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'layer', type_='foreignkey')
    op.create_foreign_key('layer_ibfk_1', 'layer', 'field', ['customer_id'], ['id'])
    op.drop_column('layer', 'field_id')
    # ### end Alembic commands ###