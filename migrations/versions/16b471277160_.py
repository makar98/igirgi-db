"""empty message

Revision ID: 16b471277160
Revises: ab9ecda03225
Create Date: 2020-08-14 16:32:01.053663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16b471277160'
down_revision = 'ab9ecda03225'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gti_quality_sheet',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gti_table_row_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gti_table_row_id'], ['gti_table_row.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_gas_research',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('interval_beg', sa.Float(), nullable=True),
    sa.Column('interval_end', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('counterfeit', sa.String(length=1024), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quality_sheet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quality_sheet_id'], ['gti_quality_sheet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_geo_research',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('interval_beg', sa.Float(), nullable=True),
    sa.Column('interval_end', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('counterfeit', sa.String(length=1024), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quality_sheet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quality_sheet_id'], ['gti_quality_sheet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_technological_research',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('interval_beg', sa.Float(), nullable=True),
    sa.Column('interval_end', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('counterfeit', sa.String(length=1024), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quality_sheet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quality_sheet_id'], ['gti_quality_sheet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_parameter',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('technological_research_row_id', sa.Integer(), nullable=False),
    sa.Column('gas_research_row_id', sa.Integer(), nullable=False),
    sa.Column('geo_research_row_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gas_research_row_id'], ['gti_gas_research.id'], ),
    sa.ForeignKeyConstraint(['geo_research_row_id'], ['gti_geo_research.id'], ),
    sa.ForeignKeyConstraint(['technological_research_row_id'], ['gti_technological_research.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('gti_format',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('parameter_id', sa.Integer(), nullable=False),
    sa.Column('technological_research_row_id', sa.Integer(), nullable=False),
    sa.Column('gas_research_row_id', sa.Integer(), nullable=False),
    sa.Column('geo_research_row_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gas_research_row_id'], ['gti_gas_research.id'], ),
    sa.ForeignKeyConstraint(['geo_research_row_id'], ['gti_geo_research.id'], ),
    sa.ForeignKeyConstraint(['parameter_id'], ['gti_parameter.id'], ),
    sa.ForeignKeyConstraint(['technological_research_row_id'], ['gti_technological_research.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gti_format')
    op.drop_table('gti_parameter')
    op.drop_table('gti_technological_research')
    op.drop_table('gti_geo_research')
    op.drop_table('gti_gas_research')
    op.drop_table('gti_quality_sheet')
    # ### end Alembic commands ###
