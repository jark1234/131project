# Importing necessary modules and components from Flask
from . import db, login
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash

# Defining the Note model
class Note(db.Model):
    # Note table columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key relationship with the User model

# Defining the User model
class User(db.Model, UserMixin):
    # User table columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)  # Storing hashed passwords for security

    dob = db.Column(db.String)  # Storing date of birth information

# User loader function for Flask-Login
@login.user_loader
def load_user(user_id):
    # Loads a user by its user ID
    return User.query.get(int(user_id))
