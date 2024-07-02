from flask import render_template, url_for, flash, redirect, request
from models.users_model import User
from db import db 
from werkzeug.security import generate_password_hash

def reset_token(token):
    user = User.verify_reset_token(token)
    if not user:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')
        if password != repeat_password:
            flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('reset_token', token=token))  # Redirect to the same token-based URL
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_token.html', token=token)
