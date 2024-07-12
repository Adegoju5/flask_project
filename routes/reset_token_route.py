from flask import render_template, url_for, flash, redirect, request
from email_utils import verify_reset_token
from db import db 
from werkzeug.security import generate_password_hash
from models.users_model import User

def reset_token(token):
    user_id = verify_reset_token(token)
    if not user_id:
        flash('That is an invalid or expired token', 'error')
        return redirect(url_for('reset_request'))
    try:
        user = User.query.filter_by(id=user_id).first()
    except:
        flash('user not found', 'error')
        return redirect(url_for('reset_request'))
    
    if request.method == 'POST':
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')
        if password != repeat_password:
            flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('reset_token', token=token)) 
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    
    return render_template('reset_token.html', token=token)
