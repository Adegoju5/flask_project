from flask import render_template, session, redirect, url_for

def remove_from_cartItem(product_id):
    if 'cart' in session:
        cart = session['cart']
        if product_id in cart:
            cart.pop(product_id)
            session['cart'] = cart
            return redirect(url_for('cart'))
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))