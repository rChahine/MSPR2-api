"""add file upload

Revision ID: a49e7aaf72b3
Revises: d11a424c75e0
Create Date: 2021-02-11 11:44:06.995497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a49e7aaf72b3'
down_revision = 'd11a424c75e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_upload',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('nom', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id_user'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('data', sa.Column('id_file', sa.Integer(), nullable=False))
    op.drop_constraint('data_id_user_fkey', 'data', type_='foreignkey')
    op.create_foreign_key(None, 'data', 'file_upload', ['id_file'], ['id'])
    op.drop_column('data', 'id_user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('data', sa.Column('id_user', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'data', type_='foreignkey')
    op.create_foreign_key('data_id_user_fkey', 'data', 'users', ['id_user'], ['id'])
    op.drop_column('data', 'id_file')
    op.drop_table('file_upload')
    # ### end Alembic commands ###
