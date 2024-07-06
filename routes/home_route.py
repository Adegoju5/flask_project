from flask import render_template, session
from models.products import Product
from db import db
import random

def home():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    products = Product.query.all()
    if len(products) >= 6:
        random_products = random.sample(products, 6)
    else:
        random_products = products 

    return render_template('home_page.html', products=random_products, no_of_cartItems=no_of_cartItems)


