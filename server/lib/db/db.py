from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from uuid import uuid4
from ..server import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)

def get_uuid():
    return uuid4().hex

karyawan_pekerjaan = db.Table('karyawan_pekerjaan',
db.Column('karyawan_id', db.String(32), db.ForeignKey('user.id')),
db.Column('pemesanan_id', db.String(32), db.ForeignKey('pemesanan.id'))
)

class User(db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(345), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    author_level = db.Column(db.Integer, nullable=False, default=2)
    no_hp = db.Column(db.String(32), nullable=False, unique=True)
    departemen_id = db.Column(db.String(32), db.ForeignKey('departemen.id'))
    meminjam = db.relationship('Peminjaman', backref='peminjam')
    pekerjaan = db.relationship('Pemesanan', secondary=karyawan_pekerjaan, backref='karyawan')
    pesanan = db.relationship('Pemesanan', backref='pelanggan')
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
def user_json(user):
    return{
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'password': user.password,
        'author_level': user.author_level,
        'no_hp': user.no_hp,
        'departemen': {'id': user.departemen.id,'name': user.departemen.name} if user.departemen else None,
        'meminjam': [peminjaman_json(pinjam)\
             for pinjam in user.meminjam] if not user.meminjam is None else {'id': user.meminjam.id},
        'pekerjaan': [pemesanan_json(kerja) for kerja in user.pekerjaan],
        'pesanan': [{'id': pesan.id, 'lokasi': pesan.lokasi, 'layanan': pesan.layanan, 'deskripsi': pesan.deskripsi,\
            'harga': pesan.harga, 'tanggal_pemesanan': pesan.tanggal_pemesanan, 'tanggal_selesai': pesan.tanggal_selesai}\
             for pesan in user.pesanan] if not user.pesanan is None else {'id': user.pesanan.id},
        'date_added': user.date_added,
    }
def user_simple(user):
        return{
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'no_hp': user.no_hp,
        }

class Inventaris(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(128), nullable=False)
    tipe = db.Column(db.String(128), nullable=False)
    peminjaman_id = db.Column(db.String(32), db.ForeignKey('peminjaman.id'))
def inventaris_json(item):
    return {
        'id': item.id,
        'name': item.name,
        'tipe': item.tipe,
        'peminjaman': {'id': item.peminjaman.id, 'peminjam': user_simple(item.peminjaman.peminjam), 'tanggal_pengembalian': item.peminjaman.tanggal_pengembalian}\
             if not item.peminjaman is None else {'id': item.peminjaman_id, 'tanggal_pengembalian': None}
    }

class Peminjaman(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    item = db.relationship('Inventaris', backref='peminjaman', uselist=False)
    peminjam_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    tanggal_pengambilan = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_pengembalian = db.Column(db.DateTime, nullable=True)
def peminjaman_json(peminjaman):
    return {
        'id': peminjaman.id,
        'item': {'id': peminjaman.item.id, 'name': peminjaman.item.name, 'tipe': peminjaman.item.name}\
             if not peminjaman.item is None else {'id': 'Barang Telah Dihapus', 'name': 'Barang Telah Dihapus'},
        'peminjam': user_simple(peminjaman.peminjam),
        'tanggal_pengambilan': peminjaman.tanggal_pengambilan,
        'tanggal_pengembalian': peminjaman.tanggal_pengembalian
    }

class Departemen(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(128), nullable=False, unique=True)
    karyawan = db.relationship('User', backref='departemen')
def departemen_json(departemen):
    return {
        'id': departemen.id,
        'name': departemen.name,
        'karyawan': [user_simple(employee) for employee in departemen.karyawan]
    }

class Pemesanan(db.Model):
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    lokasi = db.Column(db.String(345), nullable=False)
    layanan = db.Column(db.String(128), nullable=False)
    deskripsi = db.Column(db.String(345), nullable=False)
    pelanggan_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    harga = db.Column(db.String(128), nullable=True)
    estimasi_pengerjaan = db.Column(db.String(128), nullable=True)
    tanggal_pemesanan = db.Column(db.DateTime, default=datetime.utcnow)
    tanggal_selesai = db.Column(db.DateTime, nullable=True)
def pemesanan_json(order):
    return {
        'id': order.id,
        'lokasi': order.lokasi,
        'layanan': order.layanan,
        'deskripsi': order.deskripsi,
        'pelanggan': user_simple(order.pelanggan),
        'karyawan': [user_simple(employee) for employee in order.karyawan],
        'harga': order.harga,
        'estimasi_pengerjaan': order.estimasi_pengerjaan,
        'tanggal_pemesanan': order.tanggal_pemesanan,
        'tanggal_selesai': order.tanggal_selesai
    }