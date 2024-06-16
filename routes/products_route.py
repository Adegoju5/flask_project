from flask import render_template, request
from models.products import Product
from db import db


def products(category):
   
    if category:
        filtered_products = Product.query.filter_by(category=category).all()
        category= category
        return render_template( 'products.html', **locals() )
        
    filtered_products = Product.query.all()
    print(filtered_products)
    return render_template( 'products.html', filtered_products=filtered_products )