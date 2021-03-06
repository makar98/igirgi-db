"""empty message

Revision ID: 72af8cc13de3
Revises: 7201cf71a707
Create Date: 2020-08-19 14:39:53.783328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72af8cc13de3'
down_revision = '7201cf71a707'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gti_chromatograph_type',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_degasser_type',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_station_type',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('gti_table_row', sa.Column('chromatograph_type_id', sa.Integer(), nullable=True))
    op.add_column('gti_table_row', sa.Column('degasser_type_id', sa.Integer(), nullable=True))
    op.add_column('gti_table_row', sa.Column('station_type_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'gti_table_row', 'gti_chromatograph_type', ['chromatograph_type_id'], ['id'])
    op.create_foreign_key(None, 'gti_table_row', 'gti_degasser_type', ['degasser_type_id'], ['id'])
    op.create_foreign_key(None, 'gti_table_row', 'gti_station_type', ['station_type_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gti_table_row', type_='foreignkey')
    op.drop_constraint(None, 'gti_table_row', type_='foreignkey')
    op.drop_constraint(None, 'gti_table_row', type_='foreignkey')
    op.drop_column('gti_table_row', 'station_type_id')
    op.drop_column('gti_table_row', 'degasser_type_id')
    op.drop_column('gti_table_row', 'chromatograph_type_id')
    op.drop_table('gti_station_type')
    op.drop_table('gti_degasser_type')
    op.drop_table('gti_chromatograph_type')
    # ### end Alembic commands ###
