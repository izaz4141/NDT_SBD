from flask import Flask, jsonify, json, request, session
from flask_session import Session
from flask_cors import CORS, cross_origin
from config import Flask_Config
from string import ascii_letters
from datetime import datetime
from random import choice
import bcrypt

app = Flask(__name__)
app.config.from_object(Flask_Config)

from ..db import db

server_session = Session(app)
cors = CORS(app, supports_credentials=True)

@app.route("/api", methods=['GET'])
def index():
    return jsonify([*map(db.user_json, db.User.query.all())])

@cross_origin(supports_credentials=True)
@app.route("/register", methods=['POST'])
def register_user():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    no_telp = request.json['no_telp']
    password = password
    pepper = choice(ascii_letters)
    password = f"{password}{pepper}"
    user_exist = db.User.query.filter_by(email=email).first() is not None
    if user_exist:
        return jsonify({'error': 'User with that email already exist'}), 409
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    author_lv = 2
    if email.lower() == 'izazwidyan@gmail.com':
        author_lv = 0
    with app.app_context():
        new_user = db.User(name=name, email=email, password=hashed_password, author_level=author_lv, no_hp=no_telp)
        db.db.session.add(new_user)
        db.db.session.commit()
        user = db.User.query.filter_by(email=email).first()
    
    session['user_id'] = user.id

    return jsonify({
        'id': new_user.id,
        'name': new_user.name,
        'email': new_user.email
    })

@cross_origin(supports_credentials=True)
@app.route('/deleteUser', methods=["POST"])
def delete_user():
    data = request.json['id']
    u_id = request.json['u_id']
    with app.app_context():
        user = db.User.query.filter_by(id=data)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if u_id == data:
        session.pop('user_id')
    with app.app_context():
        db.User.query.filter_by(id=data).delete()
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']
    with app.app_context():
        user = db.User.query.filter_by(email=email).first()
    
    if user is None:
        return jsonify({'error': 'User not Found'}), 404
    u_pw = user.password
    benar = False
    for letter in ascii_letters:
        p_pas = f'{password}{letter}'
        if bcrypt.checkpw(p_pas.encode('utf-8'), u_pw.encode('utf-8')):
            benar = True
            break
    if benar is False:
        return jsonify({'error': 'Unaothorized'}), 401
    
    session['user_id'] = user.id

    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email
    })
@cross_origin(supports_credentials=True)
@app.route('/logout', methods=['POST'])
def logout_user():
    session.pop('user_id')
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/@me', methods=['GET'])
def get_current_user():
    user_id = session.get('user_id')

    if not user_id:
        return jsonify({'error': 'Unaothorized'}), 401

    user = db.User.query.filter_by(id=user_id).first()
    return db.user_json(user)
@cross_origin(supports_credentials=True)
@app.route('/get_user', methods=['POST'])
def get_user():
    user_id = request.json['user_id']
    with app.app_context():
        user = db.User.query.filter_by(id=user_id).first()
    return jsonify({
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'no_hp': user.no_hp,
    })
@cross_origin(supports_credentials=True)
@app.route('/get_karyawan')
def get_karyawan():
    with app.app_context():
        karyawan = db.User.query.filter_by(author_level=1)
    
    return jsonify([*map(db.user_simple, karyawan)])

@cross_origin(supports_credentials=True)
@app.route('/dev_users_list', methods=['POST'])
def dev_users_list():
    author_level = request.json['author_level']
    if author_level == 0:
        return jsonify([*map(db.user_json, db.User.query.all())])
    else:
        return jsonify({'error': 'Unaothorized'}), 401
@cross_origin(supports_credentials=True)
@app.route('/edit_user_dev', methods=['POST'])
def edit_user_dev():
    user_id = request.json['user_id']
    dev_author_level = request.json['dev_author_level']
    author_level = request.json['author_level']
    departemen_id = request.json['departemen_id']
    pekerjaan_id = request.json['pekerjaan_id']
    if dev_author_level == 0:
        with app.app_context():
            user = db.User.query.filter_by(id=user_id).first()
            if departemen_id != 'bukan':
                departemen = db.Departemen.query.filter_by(id=departemen_id).first()
                user.departemen = departemen
            if pekerjaan_id != 'bukan':
                pekerjaan = db.Pemesanan.query.filter_by(id=pekerjaan_id).first()
                user.pekerjaan.append(pekerjaan)
            user.author_level = author_level
            db.db.session.commit()
        return '200'
    else:
        return jsonify({'error': 'Unaothorized'}), 401


# Pemesanan
@cross_origin(supports_credentials=True)
@app.route('/order', methods=['POST'])
def memesan():
    lokasi = request.json['lokasi']
    layanan = request.json['layanan']
    deskripsi = request.json['deskripsi']
    user_id = request.json['user_id']

    with app.app_context():
        user = db.User.query.filter_by(id=user_id).first()
        new_order = db.Pemesanan(lokasi=lokasi, layanan=layanan, deskripsi=deskripsi, pelanggan=user)
        db.db.session.add(new_order)
        db.db.session.commit()
    
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/cancel_order', methods=['POST'])
def cancel_order():
    order_id = request.json['order_id']
    with app.app_context():
        db.Pemesanan.query.filter_by(id=order_id).delete()
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/your_order_list', methods=['POST'])
def your_order_list():
    user_id = request.json['user_id']
    with app.app_context():
        user = db.User.query.filter_by(id=user_id).first()
        order = jsonify([*map(db.pemesanan_json, user.pesanan)])
    return order, 200
@cross_origin(supports_credentials=True)
@app.route('/pemesanan_list', methods=['POST'])
def pemesanan_list():
    author_level = request.json['author_level']
    if author_level <= 1:
        item_list = jsonify([*map(db.pemesanan_json, db.Pemesanan.query.all())])
        return item_list
    else:
        return jsonify({'error': 'Not Authorized'}), 401
@cross_origin(supports_credentials=True)
@app.route('/edit_pesanan', methods=['POST'])
def edit_pesanan():
    pesanan_id = request.json['pesanan_id']
    harga = request.json['harga']
    karyawan_id = request.json['karyawan_id']
    with app.app_context():
        pesanan = db.Pemesanan.query.filter_by(id=pesanan_id).first()
        karyawan = db.User.query.filter_by(id=karyawan_id).first()
        pesanan.karyawan.append(karyawan)
        pesanan.harga = harga
        # pesanan.update({
        #     db.Pemesanan.harga: harga
        # })
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/get_kerjaan', methods=['POST'])
def get_kerjaan():
    user_id = request.json['user_id']
    author_level = request.json['author_level']
    if author_level <= 1:
        with app.app_context():
            user = db.User.query.filter_by(id=user_id).first()
            list_kerjaan = jsonify([*map(db.pemesanan_json, user.pekerjaan)])
        return list_kerjaan
    else:
        jsonify({'error': 'Not Authorized'}), 401
@cross_origin(supports_credentials=True)
@app.route('/selesai_kerja', methods=['POST'])
def selesai_kerja():
    pesanan_id = request.json['pesanan_id']
    with app.app_context():
        pesanan = db.Pemesanan.query.filter_by(id=pesanan_id).first()
        pesanan.tanggal_selesai = datetime.utcnow()
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/edit_my_kerja', methods=['POST'])
def edit_my_kerja():
    harga = request.json['harga']
    pesanan_id = request.json['pesanan_id']
    estimasi_pengerjaan = request.json['estimasi_pengerjaan']
    with app.app_context():
        pesanan = db.Pemesanan.query.filter_by(id=pesanan_id).first()
        pesanan.estimasi_pengerjaan = estimasi_pengerjaan
        pesanan.harga = harga
        db.db.session.commit()
    return '200'

# Inventaris
@cross_origin(supports_credentials=True)
@app.route('/add_inventaris', methods=['POST'])
def add_inventaris():
    name = request.json['name']
    tipe = request.json['tipe']
    with app.app_context():
        new_alat = db.Inventaris(name=name, tipe=tipe)
        db.db.session.add(new_alat)
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/remove_inventaris', methods=['POST'])
def remove_inventaris():
    item_id = request.json['item_id']
    with app.app_context():
        db.Inventaris.query.filter_by(id=item_id).delete()
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/edit_inventaris', methods=['POST'])
def edit_inventaris():
    item_id = request.json['item_id']
    name = request.json['name']
    tipe = request.json['tipe']
    with app.app_context():
        item = db.Inventaris.query.filter_by(id=item_id)
        item.update({
            db.Inventaris.name: name,
            db.Inventaris.tipe: tipe  
        })
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/inventaris_list', methods=['POST'])
def inventaris_list():
    author_level = request.json['author_level']
    if author_level <= 1:
        item_list = jsonify([*map(db.inventaris_json, db.Inventaris.query.all())])
        return item_list
    else:
        return jsonify({'error': 'Not Authorized'}), 401
# Peminjaman
@cross_origin(supports_credentials=True)
@app.route('/meminjam', methods=['POST'])
def meminjam():
    item_id = request.json['item_id']
    user_id = request.json['user_id']
    with app.app_context():
        item = db.Inventaris.query.filter_by(id=item_id).first()
        user = db.User.query.filter_by(id=user_id).first()
        peminjaman = db.Peminjaman(item=item, peminjam=user)
        db.db.session.add(peminjaman)
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/pengembalian', methods=['POST'])
def pengembalian():
    peminjaman_id = request.json['peminjaman_id']
    item_id = request.json['item_id']
    with app.app_context():
        peminjaman = db.Peminjaman.query.filter_by(id=peminjaman_id)
        item = db.Inventaris.query.filter_by(id=item_id)
        peminjaman.update({
            db.Peminjaman.tanggal_pengembalian: datetime.utcnow()    
        })
        item.update({
            db.Inventaris.peminjaman: None
        })
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/peminjaman_list', methods=['POST'])
def peminjaman_list():
    author_level = request.json['author_level']
    if author_level <= 1:
        return jsonify([*map(db.peminjaman_json, db.Peminjaman.query.all())])
    else:
        return jsonify({'error': 'Not Authorized'}), 401
# Departemen
@cross_origin(supports_credentials=True)
@app.route('/add_departemen', methods=['POST'])
def add_departemen():
    name = request.json['name']
    with app.app_context():
        new_departemen = db.Departemen(name=name)
        db.db.session.add(new_departemen)
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/remove_departemen', methods=['POST'])
def remove_departemen():
    d_id = request.json['d_id']
    with app.app_context():
        db.Departemen.query.filter_by(id=d_id).delete()
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/connect_departemen', methods=['POST'])
def connect_departemen():
    d_id = request.json['d_id']
    u_id = request.json['u_id']
    with app.app_context():
        departemen = db.Departemen.query.filter_by(id=d_id)
        user = db.User.query.filter_by(id=u_id)
        user.update({
            departemen: departemen
        })
        db.db.session.commit()
    return '200'
@cross_origin(supports_credentials=True)
@app.route('/departemen_list')
def departemen_list():
    return jsonify([*map(db.departemen_json, db.Departemen.query.all())])