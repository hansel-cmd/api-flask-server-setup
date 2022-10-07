from flask import request
from models.user import User, users_schema

def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)