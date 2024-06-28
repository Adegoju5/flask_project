from flask import render_template, request, redirect, url_for
from flask_login import login_user
from models.users_model import User
from werkzeug.security import check_password_hash

def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).one_or_none()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            return render_template('register.html')
    return render_template('login.html')

