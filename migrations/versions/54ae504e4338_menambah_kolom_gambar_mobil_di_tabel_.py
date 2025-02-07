"""Menambah kolom gambar_mobil di tabel mobil

Revision ID: 54ae504e4338
Revises: b2e5866e012f
Create Date: 2024-12-27 14:46:16.140455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54ae504e4338'
down_revision = 'b2e5866e012f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mobil', schema=None) as batch_op:
        batch_op.add_column(sa.Column('gambar_mobil', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mobil', schema=None) as batch_op:
        batch_op.drop_column('gambar_mobil')

    # ### end Alembic commands ###
