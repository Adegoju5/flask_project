import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from db import db

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=False)
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

    @hybrid_property
    def final_price(self):
        if self.discount_percentage:
            return self.price * (1 - self.discount_percentage / 100.0)
        return self.price

    def __repr__(self):
        return f'<Product {self.name}>'


    
