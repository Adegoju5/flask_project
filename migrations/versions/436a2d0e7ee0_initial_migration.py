"""Initial migration

Revision ID: 436a2d0e7ee0
Revises: 
Create Date: 2024-07-08 20:37:46.774360

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '436a2d0e7ee0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.drop_column('final_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('final_price', sa.NUMERIC(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
