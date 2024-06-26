from flask import render_template, request
from models.products import Product
from db import db


def products(argument):
    filter_by_category = Product.query.filter_by(category=argument).all()
    if filter_by_category:
        filtered_products = filter_by_category
        return render_template( 'products.html', filtered_products=filtered_products)
    filtered_product = Product.query.filter_by(id=argument).one_or_none()
    if filtered_product:
        name = filtered_product.name
        color = filtered_product.color
        size = filtered_product.size

        similar_products_in_size = db.session.query(Product.size).filter(
            Product.name == name,
            Product.color == color,
            Product.id != filtered_product.id
        ).distinct().all()

        similar_products_in_color = db.session.query(Product.color).filter(
            Product.name == name, 
            Product.size == size,  
            Product.id != filtered_product.id
        ).distinct().all()

        similar_products_in_size = [filtered_product.size] + [s[0] for s in similar_products_in_size if s[0] != filtered_product.size]
        similar_products_in_color = [filtered_product.color] + [c[0] for c in similar_products_in_color if c[0] != filtered_product.color]
        return render_template('product.html', filtered_product=filtered_product, similar_products_in_size=similar_products_in_size, similar_products_in_color=similar_products_in_color)