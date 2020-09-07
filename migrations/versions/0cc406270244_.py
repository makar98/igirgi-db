"""empty message

Revision ID: 0cc406270244
Revises: 53c7fe3c2a6f
Create Date: 2020-08-20 15:51:18.333835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cc406270244'
down_revision = '53c7fe3c2a6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gti_table_row_quality',
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('edit_date', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('gti_table_row', sa.Column('quality', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'gti_table_row', 'gti_table_row_quality', ['quality'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gti_table_row', type_='foreignkey')
    op.drop_column('gti_table_row', 'quality')
    op.drop_table('gti_table_row_quality')
    # ### end Alembic commands ###