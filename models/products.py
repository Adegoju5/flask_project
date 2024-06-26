import uuid
from sqlalchemy.dialects.postgresql import UUID
from db import db

class Product(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(30), nullable=True)
    type = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    size = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)
    is_discount = db.Column(db.Boolean, default=False, nullable=False) 
    discount_percentage = db.Column(db.Float, nullable=True) 

    def __repr__(self):
        return f'<Product {self.name}>'


    
