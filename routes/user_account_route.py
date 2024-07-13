from flask import render_template, session
from flask_login import login_required, current_user
from models.users_model import User


@login_required
def user_account():
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('user_account.html', user=current_user, no_of_cartItems=no_of_cartItems)