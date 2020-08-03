"""empty message

Revision ID: dde38fc86db6
Revises: e2f5787a58f0
Create Date: 2020-04-18 15:06:40.209234

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dde38fc86db6'
down_revision = 'e2f5787a58f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('wellbore_type_ibfk_1', 'wellbore_type', type_='foreignkey')
    op.drop_column('wellbore_type', 'wellbore_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wellbore_type', sa.Column('wellbore_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('wellbore_type_ibfk_1', 'wellbore_type', 'wellbore', ['wellbore_id'], ['id'])
    # ### end Alembic commands ###
