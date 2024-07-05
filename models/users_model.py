# models/users_model.py

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    telephone = db.Column(db.String(20), nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=True)
    post_code = db.Column(db.String(250), nullable=True)
    delivery_address = db.Column(db.String(250), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    
    def get_reset_token(self, expires_sec=1800):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return s.dumps(str(self.id), salt='reset-password')

    @staticmethod
    def verify_reset_token(token):
        s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, salt='reset-password', max_age=1800)
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
