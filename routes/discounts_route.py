from flask import render_template
from models.products import Product
from db import db


def discounts():
    discounted_products = Product.query.filter_by(is_discount=True).all()
    return render_template( 'products.html', discounted_products=discounted_products )