import os
from flask import Flask, request, jsonify, abort, flash
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename

import sys
from connection.connection import db, ma
from routes.routes import *
from dotenv import load_dotenv

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.env'))
load_dotenv(dotenv_path)



# Init app
app = Flask(__name__)

# config database
# syntax: 'mysql://username:password@localhost/db_name'
# NOTE: These credentials need to be inside the .env file
#           Create your own .env file
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQL_ALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

# Secret Key
# NOTE: I am not sure what this is for
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Init bcrypt
bcrypt = Bcrypt(app)

# Init db
db.init_app(app)

# Init ma
ma.init_app(app)

# Import modules to be executed in each url rule
from controllers import get_specific_user, index, add_user, get_users, update_user, delete_user

# Index
app.add_url_rule(INDEX, 'index', index.main, methods = ['GET'])

# Add User
app.add_url_rule(ADD_USER, 'add_user', add_user.add, methods = ['POST'])

# Get all users
app.add_url_rule(GET_ALL_USERS, 'get_all_users', get_users.get_users, methods = ['GET'])

# Get specific user
app.add_url_rule(GET_SPECIFIC_USER, 'get_specific_user', get_specific_user.get_user, methods = ['GET'])

# Update a specific user
app.add_url_rule(UPDATE_SPECIFIC_USER, 'update_specific_user', update_user.update_user, methods = ['PUT'])

# Delete a specific user
app.add_url_rule(DELETE_SPECIFIC_USER, 'delete_user', delete_user.delete_user, methods = ['DELETE'])




# To create database tables inside the database,
# run the command: python server.py --create-db
if len(sys.argv) > 1 and sys.argv[1] == "--create-db":
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
