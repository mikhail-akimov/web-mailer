"""empty message

Revision ID: f431c403ce50
Revises: afe8d4a42410
Create Date: 2018-12-18 14:20:40.181261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f431c403ce50'
down_revision = 'afe8d4a42410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('event', sa.Column('owner', sa.Integer(), nullable=True))
    op.add_column('event', sa.Column('recipients', sa.Integer(), nullable=True))
    op.add_column('event', sa.Column('title', sa.String(length=120), nullable=True))
    op.create_foreign_key(None, 'event', 'recipients_group', ['recipients'], ['id'])
    op.create_foreign_key(None, 'event', 'user', ['owner'], ['id'])
    op.drop_column('event', 'last_seen')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('last_seen', sa.DATETIME(), nullable=True))
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_constraint(None, 'event', type_='foreignkey')
    op.drop_column('event', 'title')
    op.drop_column('event', 'recipients')
    op.drop_column('event', 'owner')
    op.drop_column('event', 'date')
    # ### end Alembic commands ###