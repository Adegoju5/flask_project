from flask import render_template, request, session
from models.products import Product

def cart():
    cart = session['cart']
    list_of_products = []
    for key, item in cart.items():
        product = Product.query.filter_by(id=key).one()
        product.quantity = item
        list_of_products.append(product)
    return render_template('cart_page.html', cart=list_of_products)