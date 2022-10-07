from models.user import User, user_schema

def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)