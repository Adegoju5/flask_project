from flask import render_template, session, redirect, url_for

def add_to_cartItem(product_id):
    print(product_id, 'alex')
    if 'cart' not in session:
        session['cart'] = {}
    pass
    cart = session['cart']
    if product_id in cart:
        cart[product_id] += 1
        session['cart'] = cart
        return redirect(url_for('cart'))
    cart[product_id] = 1
    session['cart'] = cart
    return redirect(url_for('cart'))