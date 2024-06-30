from flask import request, jsonify, render_template
from models.products import Product
from db import db

def change_product():
    color = request.args.get('color')
    name = request.args.get('name')
    size = request.args.get('size')
    print(size, name, color)
    
    if color and name and size:
        filtered_product = Product.query.filter_by(color=color, name=name, size=size).one_or_none()
        print(filtered_product)
        
        if filtered_product:
            similar_products_in_size = db.session.query(Product.size).filter(
                Product.color == filtered_product.color,
                Product.name == filtered_product.name
            ).distinct().all()
            print(similar_products_in_size, 'wura')
            
            similar_products_in_color = db.session.query(Product.color).filter(
                Product.name == filtered_product.name,
                Product.size == filtered_product.size
            ).distinct().all()
            print(similar_products_in_color)
            
            similar_products_in_size = [filtered_product.size] + [s[0] for s in similar_products_in_size if s[0] != filtered_product.size]
            similar_products_in_color = [filtered_product.color] + [c[0] for c in similar_products_in_color if c[0] != filtered_product.color]
            print(filtered_product, similar_products_in_color, similar_products_in_size, 'alex')
            

            response = {
                'filtered_product': {
                    'name': filtered_product.name,
                    'price': filtered_product.price,
                    'image_path': filtered_product.image_path
                },
                'similar_products_in_size': similar_products_in_size,
                'similar_products_in_color': similar_products_in_color
            }
            print(response)
            
            return jsonify(response)
    
    return render_template('login.html')