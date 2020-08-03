"""empty message

Revision ID: 870d7ec73185
Revises: e14b7996f6e1
Create Date: 2020-05-11 17:43:33.754020

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '870d7ec73185'
down_revision = 'e14b7996f6e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('suite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('change_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'field_id', name='unique_suite')
    )
    op.add_column('layer', sa.Column('suite_id', sa.Integer(), nullable=False))
    op.drop_constraint('unique_layer', 'layer', type_='unique')
    op.create_unique_constraint('unique_layer', 'layer', ['name', 'suite_id'])
    op.drop_constraint('layer_ibfk_1', 'layer', type_='foreignkey')
    op.create_foreign_key(None, 'layer', 'suite', ['suite_id'], ['id'])
    op.drop_column('layer', 'field_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('layer', sa.Column('field_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'layer', type_='foreignkey')
    op.create_foreign_key('layer_ibfk_1', 'layer', 'field', ['field_id'], ['id'])
    op.drop_constraint('unique_layer', 'layer', type_='unique')
    op.create_unique_constraint('unique_layer', 'layer', ['name', 'field_id'])
    op.drop_column('layer', 'suite_id')
    op.drop_table('suite')
    # ### end Alembic commands ###
