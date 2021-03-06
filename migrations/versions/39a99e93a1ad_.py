"""empty message

Revision ID: 39a99e93a1ad
Revises: dde38fc86db6
Create Date: 2020-04-18 15:06:59.621027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39a99e93a1ad'
down_revision = 'dde38fc86db6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wellbore_type', sa.Column('wellbore_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'wellbore_type', 'wellbore', ['wellbore_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'wellbore_type', type_='foreignkey')
    op.drop_column('wellbore_type', 'wellbore_id')
    # ### end Alembic commands ###
