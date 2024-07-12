# models/users_model.py

import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db
from flask_login import UserMixin


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
    

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
