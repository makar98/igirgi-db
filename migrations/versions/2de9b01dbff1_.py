"""empty message

Revision ID: 2de9b01dbff1
Revises: ef6d1b639a64
Create Date: 2020-08-10 12:04:17.726507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2de9b01dbff1'
down_revision = 'ef6d1b639a64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('editable_field', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('editable_field', sa.Column('edit_date', sa.DateTime(), nullable=True))
    op.add_column('logger', sa.Column('create_date', sa.DateTime(), nullable=True))
    op.add_column('logger', sa.Column('edit_date', sa.DateTime(), nullable=True))
    op.drop_column('logger', 'date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('logger', sa.Column('date', mysql.DATETIME(), nullable=True))
    op.drop_column('logger', 'edit_date')
    op.drop_column('logger', 'create_date')
    op.drop_column('editable_field', 'edit_date')
    op.drop_column('editable_field', 'create_date')
    # ### end Alembic commands ###
