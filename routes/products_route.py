from flask import render_template, request
from models.products import Product
from db import db


def products(argument):
    filter_by_category = Product.query.filter_by(category=argument).all()
    if filter_by_category:
        filtered_products = filter_by_category
        return render_template( 'products.html', filtered_products=filtered_products)
    
    filtered_product = Product.query.filter_by(id=argument).one()
    return render_template( 'product.html', filtered_product=filtered_product )