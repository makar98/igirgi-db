"""empty message

Revision ID: 23d312eb4654
Revises: 72af8cc13de3
Create Date: 2020-08-19 15:05:39.570495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23d312eb4654'
down_revision = '72af8cc13de3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'gti_chromatograph_type', ['name'])
    op.create_unique_constraint(None, 'gti_degasser_type', ['name'])
    op.create_unique_constraint(None, 'gti_service_company', ['name'])
    op.create_unique_constraint(None, 'gti_station_type', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gti_station_type', type_='unique')
    op.drop_constraint(None, 'gti_service_company', type_='unique')
    op.drop_constraint(None, 'gti_degasser_type', type_='unique')
    op.drop_constraint(None, 'gti_chromatograph_type', type_='unique')
    # ### end Alembic commands ###