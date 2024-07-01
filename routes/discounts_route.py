from flask import render_template, session
from models.products import Product
from db import db


def discounts():
    discounted_products = Product.query.filter_by(is_discount=True).all()
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('discounts.html', discounted_products=discounted_products, no_of_cartItems=no_of_cartItems)