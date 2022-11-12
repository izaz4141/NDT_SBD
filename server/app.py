from flask import Flask, jsonify, json, request, session
from flask_session import Session
from flask_cors import CORS, cross_origin
from string import ascii_letters
import bcrypt

from helpers import *
from config import Flask_Config
from util import db

app = Flask(__name__)
app.config.from_object(Flask_Config)
cors = CORS(app, supports_credentials=True)
server_session = Session(app)

@app.route('/users')
def get_users():
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''
    data = query_get_users()
    data = raw_data_to_json(data)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users/<int:id>')
def get_user_by_id(id):
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''

    data = query_get_user_by_id(id)
    data = raw_data_to_json(data)[0]
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/users', methods=['POST'])
def register_user():
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''

    # Default response and status
    response = {
        "description": "user has been created successfully"
    }
    status = 201
    
    # Get request data
    data = request.get_json()
    # Check request data
    if not "name" in data or not "address" in data:
        # Response and status for bad request
        response = {
            "description": "malformed data"
        }
        status = 400
        response = app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )
        return response
    
    query_post_user(data)
    # Response and status for success request
    response = app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )
    return response

@app.route('/users/<int:id>', methods=['PUT'])
def edit_user(id):
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''

    # Default response and status
    response = {
        "description": "user has been updated successfully"
    }
    status = 200

    query_edit_user_by_id(id)
    
    # Response and status for success request
    response = app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )
    return response

@app.route('/users/<int:id>', methods=['PATCH'])
def edit_user_by_field(id):
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''

    # Default response and status
    response = {
        "description": "user has been updated successfully"
    }
    status = 200

    query_patch_user_by_id(id)
    
    # Response and status for success request
    response = app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )
    return response

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    '''
    Connect to db
    Do the select query to database
    Close connection when already used db
    '''
    
    # Default response and status
    response = {
        "description": "user has been deleted successfully"
    }
    status = 200

    query_delete_user_by_id(id)
    
    # Response and status for success request
    response = app.response_class(
            response=json.dumps(response),
            status=status,
            mimetype='application/json'
        )
    return response


@cross_origin(supports_credentials=True)
@app.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']

    data = db.records("SELECT * FROM Users WHERE email = ?", email)
    data = query_get_user_by_id(id)
    data = raw_data_to_json(data)[0]

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
if __name__ == '__main__':
    app.run(debug=True, port=5055)