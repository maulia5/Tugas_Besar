"""Membuat Semua Tabel yang Diperlukan

Revision ID: b2e5866e012f
Revises: 
Create Date: 2024-12-27 13:51:50.901673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2e5866e012f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mobil',
    sa.Column('mobil_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('merk', sa.String(length=255), nullable=False),
    sa.Column('deskripsi_mobil', sa.String(length=255), nullable=False),
    sa.Column('harga_mobil', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('mobil_id')
    )
    op.create_table('penyewa',
    sa.Column('penyewa_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nama_penyewa', sa.String(length=255), nullable=False),
    sa.Column('no_telepon', sa.String(length=15), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('penyewa_id')
    )
    op.create_table('transaksi',
    sa.Column('transaksi_id', sa.Integer(), nullable=False),
    sa.Column('tanggal_mulai', sa.DateTime(), nullable=False),
    sa.Column('tanggal_selesai', sa.DateTime(), nullable=False),
    sa.Column('biaya_tambahan', sa.Integer(), nullable=False),
    sa.Column('total_biaya', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('penyewa_id', sa.Integer(), nullable=False),
    sa.Column('mobil_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['mobil_id'], ['mobil.mobil_id'], ),
    sa.ForeignKeyConstraint(['penyewa_id'], ['penyewa.penyewa_id'], ),
    sa.PrimaryKeyConstraint('transaksi_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaksi')
    op.drop_table('penyewa')
    op.drop_table('mobil')
    # ### end Alembic commands ###