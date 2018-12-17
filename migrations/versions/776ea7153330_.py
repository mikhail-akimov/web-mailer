"""empty message

Revision ID: 776ea7153330
Revises: 
Create Date: 2018-12-13 16:51:04.879736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '776ea7153330'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_table')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_table',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('last_seen', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
