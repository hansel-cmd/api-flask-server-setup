from connection.connection import db, ma
from datetime import datetime

# User Class/Model
class User(db.Model):
    """
    This is a database model.
    """
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(20), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.now())

    def __repr__(self):
        return '<Name %r>' % self.name

    def __init__(self, name, email):
        self.name = name
        self.email = email


# User Schema
class UserSchema(ma.Schema):
    """This is a database schema."""
    class Meta:
        """Specify which fields you want to see in RESTful API"""
        fields = ('id', 'name', 'email', 'date_added')


user_schema = UserSchema()
users_schema = UserSchema(many = True)