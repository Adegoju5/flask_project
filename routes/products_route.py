from flask import render_template, request
from models.products import Product
from db import db


def products(argument):
    filter_by_category = Product.query.filter_by(category=argument).all()
    if filter_by_category:
        filtered_products = filter_by_category
        return render_template( 'products.html', filtered_products=filtered_products)
    
    filtered_product = Product.query.filter_by(id=argument).one_or_none()
    desc= filtered_product.description
    color= filtered_product.color
    print(color)
    size = filtered_product.size
    print(size)
    similar_products_in_size = db.session.query(Product.size).filter(
                Product.color == color,
                Product.description == desc
            ).distinct().all()
            
    similar_products_in_color = db.session.query(Product.color).filter(
                Product.size == size,
                Product.description == desc
            ).distinct().all()
    similar_products_in_sizes = [ size[0] for size in similar_products_in_size ]
    similar_products_in_color = [ color[0] for color in similar_products_in_color ]
    print(similar_products_in_color)
    print(similar_products_in_size)
    return render_template( 'product.html', **locals() )