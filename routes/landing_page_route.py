from flask import render_template, session

def landing_page():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('landing_page.html', no_of_cartItems=no_of_cartItems)