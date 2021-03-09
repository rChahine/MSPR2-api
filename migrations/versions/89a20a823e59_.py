"""empty message

Revision ID: 89a20a823e59
Revises: a49e7aaf72b3
Create Date: 2021-03-09 12:41:16.210763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '89a20a823e59'
down_revision = 'a49e7aaf72b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data', sa.Column('uniquId', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('data', 'uniquId')
    # ### end Alembic commands ###