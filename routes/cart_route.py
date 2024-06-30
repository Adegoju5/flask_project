from flask import render_template, session
from models.products import Product

def cart():
    if 'cart' not in session:
        total={}
        total['price'] = 0
        total['no_of_items'] = 0
        return render_template('cart_page.html', cart=[], cart_total=total)
    list_of_products = []
    total = {}
    cart_total_sum = 0
    cart_total_item = 0
    cart = session['cart']
    for key, item in cart.items():
        product = Product.query.filter_by(id=key).one()
        product.quantity = item
        cart_total_sum += product.price * item
        cart_total_item += item
        list_of_products.append(product)
    total['price'] = cart_total_sum
    total['no_of_items'] = cart_total_item
    return render_template('cart_page.html', cart=list_of_products, cart_total=total)

