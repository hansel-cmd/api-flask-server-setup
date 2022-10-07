from flask import request
from models.user import User, user_schema
from connection.connection import db

def add():
    user_data = request.get_json()
    user = User(name = user_data['name'], email = user_data['email'])
    db.session.add(user)
    db.session.commit()

    return user_schema.jsonify(user)