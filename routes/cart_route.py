from flask import render_template, request

def cart():
    return render_template('cart_page.html')