from flask_login import  login_required, current_user
from flask import redirect, url_for, request, flash, render_template
from models.users_model import User
from werkzeug.security import check_password_hash
from db import db
from sqlalchemy.exc import SQLAlchemyError
import uuid

@login_required
def delete_user():
    if request.method == 'POST':
        password=request.form.get('password')
        repeat_password=request.form.get('repeat_password')
        if password != repeat_password:
            flash('passwords does not match', 'error')
            return redirect(url_for('delete_user'))
        user=User.query.filter_by(id=current_user.id).first()
        if not user:
            flash('user not found')
            return redirect(url_for('delete_user'))
        if not check_password_hash(user.password, password):
            flash('password incorrect')
            return redirect(url_for('delete_user'))
        try:
            db.session.delete(user)
            db.session.commit()
            flash('User deleted successfully', 'success')
            return redirect(url_for('login'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash('server error', 'error')
            return redirect(url_for('delete_user'))
    return render_template('delete_user.html')
