import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender = db.Column(db.String, nullable=False)
    telephone = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)  # Ensure the type is Date
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(30), nullable=False)
    home_address = db.Column(db.String(200), nullable=False)
    delivery_address = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

