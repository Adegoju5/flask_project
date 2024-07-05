from flask import render_template, request, redirect, url_for, flash, session
from db import db
from models.users_model import User
from werkzeug.security import generate_password_hash
from utilities.email_check_util import is_functional_email

def register():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        if not isinstance(first_name, str) or not first_name.isalpha():
            flash("invalid value for first_name", "error")
            return redirect(url_for('register'))
        last_name = request.form['last_name']
        if not isinstance(first_name, str) or not first_name.isalpha():
            flash("invalid value for last name", "error")
            return redirect(url_for('register'))
        email = request.form['email']
        if not is_functional_email:
            flash("invalid email", "error")
            return redirect(url_for('register'))
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        
        if not password:
            flash("password cannot be empty", "error")
            return redirect(url_for('register'))
        
        if password != repeat_password:
            flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('register'))

        new_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("you've been successfully registered", "success")
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error registering user: {str(e)}', 'error')
            return redirect(url_for('register'))
            
    return render_template('register.html', no_of_cartItems=no_of_cartItems)

