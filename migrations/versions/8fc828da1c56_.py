"""empty message

Revision ID: 8fc828da1c56
Revises: 735cbec3c99d
Create Date: 2020-04-15 12:18:43.178637

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '8fc828da1c56'
down_revision = '735cbec3c99d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wellbore_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('change_date', sa.DateTime(), nullable=True),
    sa.Column('wellbore_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['wellbore_id'], ['wellbore.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('well_type')
    op.drop_constraint('unique_well', 'well', type_='unique')
    op.create_unique_constraint('unique_well', 'well', ['name', 'field_id', 'pad_id', 'customer_id'])
    op.drop_constraint('well_ibfk_4', 'well', type_='foreignkey')
    op.drop_column('well', 'well_type_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('well', sa.Column('well_type_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.create_foreign_key('well_ibfk_4', 'well', 'well_type', ['well_type_id'], ['id'])
    op.drop_constraint('unique_well', 'well', type_='unique')
    op.create_unique_constraint('unique_well', 'well', ['name', 'field_id', 'pad_id', 'customer_id', 'well_type_id'])
    op.create_table('well_type',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('wellbore_type')
    # ### end Alembic commands ###
