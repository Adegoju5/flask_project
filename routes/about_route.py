from flask import render_template, request, session

def about():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('about.html', no_of_cartItems=no_of_cartItems)