from flask import render_template, session
from flask_login import login_required, current_user
from models.users_model import User


@login_required
def user_account():
    return render_template('user_account.html', user=current_user)