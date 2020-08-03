"""empty message

Revision ID: 7922f9c71814
Revises: 39a99e93a1ad
Create Date: 2020-04-18 15:10:43.768004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7922f9c71814'
down_revision = '39a99e93a1ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_wellbore_type', 'wellbore', ['name', 'well_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_wellbore_type', 'wellbore', type_='unique')
    # ### end Alembic commands ###
