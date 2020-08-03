"""empty message

Revision ID: a19ede0e4127
Revises: 8210d55f7a69
Create Date: 2020-04-14 15:22:41.658635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a19ede0e4127'
down_revision = '8210d55f7a69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('well', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('well', sa.Column('field_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'well', 'customer', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'well', 'field', ['field_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'well', type_='foreignkey')
    op.drop_constraint(None, 'well', type_='foreignkey')
    op.drop_column('well', 'field_id')
    op.drop_column('well', 'customer_id')
    # ### end Alembic commands ###
