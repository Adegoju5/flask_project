from flask import render_template
from models.products import Product
from db import db


def discounts():
    filtered_products = Product.query.filter_by(is_discount=True).all()
    return render_template( 'products.html', filtered_products=filtered_products )