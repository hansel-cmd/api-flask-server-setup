from flask import request
from models.user import User, user_schema
from connection.connection import db

def update_user(id):
    user_data = request.get_json()

    user = User.query.get(id)
    user.name = user_data['name']
    user.email = user_data['email']

    db.session.commit()

    return user_schema.jsonify(user)