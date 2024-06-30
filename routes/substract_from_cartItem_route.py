from flask import render_template, session, redirect, url_for

def substract_from_cartItem(product_id):
    if 'cart' in session:
        cart = session['cart']
        if product_id in cart:
            if cart[product_id] > 1 :
                cart[product_id] -= 1
                session['cart'] = cart
                return redirect(url_for('cart'))
            return redirect(url_for('cart'))
        return redirect(url_for('cart'))

