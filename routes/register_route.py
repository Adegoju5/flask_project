from flask import render_template, request, redirect, url_for, flash
from db import db
from models.users_model import User
from werkzeug.security import generate_password_hash

def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        gender = request.form['gender']
        telephone = request.form['telephone']
        date_of_birth = request.form['dob']
        email = request.form['email']
        age = request.form['age']
        country = request.form['country']
        home_address = request.form['home_address']
        delivery_address = request.form['delivery_address']
        password = request.form['password']
        repeat_password = request.form['repeat_password']
        
        if password != repeat_password:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect(url_for('register'))
        
        # Do not assign id directly, let SQLAlchemy handle it
        new_user = User(
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            telephone=telephone,
            date_of_birth=date_of_birth,
            email=email,
            age=age,
            country=country,
            home_address=home_address,
            delivery_address=delivery_address,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error registering user: {str(e)}', 'error')
            return redirect(url_for('register'))
            
    return render_template('register.html')

