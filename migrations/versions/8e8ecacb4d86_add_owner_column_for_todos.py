"""Add owner column for todos

Revision ID: 8e8ecacb4d86
Revises: 4f74111c330d
Create Date: 2024-03-28 00:32:50.162108

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e8ecacb4d86'
down_revision = '4f74111c330d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('owner', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todos', schema=None) as batch_op:
        batch_op.drop_column('owner')

    # ### end Alembic commands ###
