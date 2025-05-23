from flask_sqlalchemy import SQLAlchemy
from flask import current_app as app
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask_security import UserMixin, RoleMixin
from datetime import datetime

db = SQLAlchemy()

# Association table for many-to-many User <-> Role
class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(64), unique=True, nullable=False)
    
    roles = db.relationship('Role', secondary='user_roles', backref='bearers')
    user_detail = db.relationship('UserDetail', backref='user', uselist=False, lazy=True)

    def get_reset_token(self, expires_sec=300):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}, salt=app.config['SECURITY_PASSWORD_SALT'])

    @staticmethod
    def verify_reset_token(token, max_age=300):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age=max_age)
            return User.query.get(data['user_id'])
        except Exception:
            return None
    
class UserDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=True)
    dob = db.Column(db.Date, nullable=True)
    bio = db.Column(db.Text, nullable=True) 
    gender = db.Column(db.String(10), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())
