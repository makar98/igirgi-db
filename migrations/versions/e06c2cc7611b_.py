"""empty message

Revision ID: e06c2cc7611b
Revises: 0cc406270244
Create Date: 2020-08-20 16:24:10.169715

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e06c2cc7611b'
down_revision = '0cc406270244'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('gti_table_row', 'degasser')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gti_table_row', sa.Column('degasser', mysql.VARCHAR(length=128), nullable=True))
    # ### end Alembic commands ###
