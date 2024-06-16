from flask import render_template 
from models.products import Product
from db import db

def categories():
    products = db.session.query(Product.category).distinct().all()
    category_list = [ product[0] for product in products ]
    return render_template('categories.html', category_list=category_list)