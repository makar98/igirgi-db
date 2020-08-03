"""empty message

Revision ID: b1466c8dea35
Revises: 55ec14805961
Create Date: 2020-04-13 16:51:00.105054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1466c8dea35'
down_revision = '55ec14805961'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('well_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pad',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('well',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('field_id', sa.Integer(), nullable=False),
    sa.Column('pad_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('service_company_id', sa.Integer(), nullable=False),
    sa.Column('well_type_id', sa.Integer(), nullable=False),
    sa.Column('country', sa.String(length=256), nullable=True),
    sa.Column('serial_number', sa.String(length=256), nullable=True),
    sa.Column('well_num', sa.String(length=256), nullable=True),
    sa.Column('wellbore_number', sa.String(length=256), nullable=True),
    sa.Column('status', sa.String(length=256), nullable=True),
    sa.Column('altitude', sa.String(length=256), nullable=True),
    sa.Column('x_coordinate', sa.String(length=256), nullable=True),
    sa.Column('y_coordinate', sa.String(length=256), nullable=True),
    sa.Column('well_log_beg_date', sa.DateTime(), nullable=True),
    sa.Column('well_log_end_date', sa.DateTime(), nullable=True),
    sa.Column('_Well__total_depth', sa.String(length=256), nullable=True),
    sa.Column('description_part_1', sa.String(length=256), nullable=True),
    sa.Column('description_part_2', sa.String(length=256), nullable=True),
    sa.Column('description_part_3', sa.String(length=256), nullable=True),
    sa.Column('description_part_4', sa.String(length=256), nullable=True),
    sa.Column('description_part_5', sa.String(length=256), nullable=True),
    sa.Column('description_part_6', sa.String(length=256), nullable=True),
    sa.Column('description_part_7', sa.String(length=256), nullable=True),
    sa.Column('description_part_8', sa.String(length=256), nullable=True),
    sa.Column('description_part_9', sa.String(length=256), nullable=True),
    sa.Column('toolstring', sa.String(length=256), nullable=True),
    sa.Column('total_depth', sa.Float(), nullable=True),
    sa.Column('bit_size', sa.Float(), nullable=True),
    sa.Column('casing_shoe', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.ForeignKeyConstraint(['field_id'], ['field.id'], ),
    sa.ForeignKeyConstraint(['pad_id'], ['pad.id'], ),
    sa.ForeignKeyConstraint(['service_company_id'], ['service_company.id'], ),
    sa.ForeignKeyConstraint(['well_type_id'], ['well_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('well')
    op.drop_table('pad')
    op.drop_table('well_type')
    # ### end Alembic commands ###
