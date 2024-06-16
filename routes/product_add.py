# flask_project/routes/product_add.py
from flask import render_template, request, redirect, session 
from db import db  # Import db from db.py
from models.products import Product
from uuid import uuid4

def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']
        category = request.form['category']
        brand = request.form['brand']
        type = request.form['type']
        color = request.form['color']
        size = request.form['size']
        image_path = request.form['image_path']

        new_product = Product(
        id=uuid4(),
        name=name,
        description=description,
        price=price,
        quantity=quantity,
        category=category,
        brand=brand,
        type=type,
        color=color,
        size=size,
        image_path=image_path
        )
        db.session.add(new_product)
        db.session.commit()
        print(new_product)
        return redirect('/login')
    return render_template('product_add.html')


