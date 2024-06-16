from flask import render_template
from models.products import Product
from db import db


def discounts():
    discounted_products = Product.query.filter_by(is_discount=True).all()
    print(discounted_products)
    return render_template('discounts.html', discounted_products=discounted_products)