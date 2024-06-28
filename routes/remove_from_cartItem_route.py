from flask import render_template, session, redirect, url_for

def remove_from_cartItem(product_id):
    cart = session['cart']
    if product_id in cart:
        if cart[product_id] > 1 :
            cart[product_id] -= 1
            return redirect(url_for('cart'))
        return redirect(url_for('cart'))
    return redirect(url_for('cart'))
