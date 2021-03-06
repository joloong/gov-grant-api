"""empty message

Revision ID: 631a7fd5be14
Revises: 
Create Date: 2021-09-04 15:27:06.236212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '631a7fd5be14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('households',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('postal_code', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('unit', sa.Integer(), nullable=False),
    sa.Column('housing_type', sa.String(), nullable=False),
    sa.CheckConstraint("housing_type in ('HDB', 'Condominium', 'Landed')"),
    sa.CheckConstraint('level >= 0 and level <= 999999'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('postal_code', 'level', 'unit')
    )
    op.create_table('members',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('marital_status', sa.String(), nullable=False),
    sa.Column('occupation_type', sa.String(), nullable=False),
    sa.Column('annual_income', sa.Integer(), nullable=False),
    sa.Column('dob', sa.Date(), nullable=False),
    sa.CheckConstraint("gender in ('male', 'female')"),
    sa.CheckConstraint("marital_status in ('single', 'married', 'divorced')"),
    sa.CheckConstraint("occupation_type in ('employed', 'unemployed', 'student')"),
    sa.CheckConstraint('annual_income >= 0'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('families',
    sa.Column('household_id', sa.Integer(), nullable=False),
    sa.Column('member_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['household_id'], ['households.id'], ),
    sa.ForeignKeyConstraint(['member_id'], ['members.id'], ),
    sa.PrimaryKeyConstraint('household_id', 'member_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('families')
    op.drop_table('members')
    op.drop_table('households')
    # ### end Alembic commands ###
