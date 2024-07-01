from flask import render_template , session
from models.products import Product
from db import db

def categories():
    products = db.session.query(Product.category).distinct().all()
    category_list = [ product[0] for product in products ]
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('categories.html', category_list=category_list, no_of_cartItems=no_of_cartItems)
    