from flask import render_template, session
from models.products import Product
import uuid

def cart():
    if 'cart' not in session:
        return render_template('cart_page.html', cart={})
    list_of_products = []
    total = {}
    cart_total_sum = 0
    cart_total_item = 0
    cart = session['cart']
    for key, value in cart.items():
        product = Product.query.filter_by(id=key).one()
        if not product:
            continue
        product.quantity= value
        cart_total_sum += product.final_price * value
        cart_total_item += value
        list_of_products.append(product)
    total['price'] = cart_total_sum
    total['no_of_items'] = cart_total_item
    session['total'] = total
    return render_template('cart_page.html', cart=list_of_products, cart_total_price=cart_total_sum, no_of_cartItems=cart_total_item if cart_total_item else '')

