from flask import render_template, request, redirect, url_for, session
from flask_login import login_user
from models.users_model import User
from werkzeug.security import check_password_hash

def login():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).one_or_none()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('register.html', no_of_cartItems=no_of_cartItems)
    return render_template('login.html', no_of_cartItems=no_of_cartItems)

