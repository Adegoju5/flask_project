from flask import render_template, request, redirect, url_for, flash, session
from db import db
from models.users_model import User
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user
from utilities.phone_check_util import is_valid_phone_number
from utilities.country_check_util import is_valid_country
from utilities.postal_code_check_util import is_valid_postal_code
from utilities.address_check_util import is_valid_address
from datetime import datetime 

@login_required
def update_user_profile():
    print('alex')
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        if not isinstance(first_name, str) or not first_name.isalpha():
            flash("Invalid first name value", "error")
            return redirect(url_for('update_user_profile'))
        last_name = request.form['last_name']
        if not isinstance(last_name, str) or not last_name.isalpha():
            flash("Invalid last name value", "error")
            return redirect(url_for('update_user_profile'))
        gender = request.form['gender']
        if gender:
            if gender not in ["male", "female", "other"]:
                flash("Invalid gender", "error")
                return redirect(url_for("update_user_profile"))
        telephone = request.form['telephone']
        if telephone:
            if not is_valid_phone_number(telephone):
                print(is_valid_phone_number(telephone))
                flash("Invalid telephone number", "error")
                return redirect(url_for("update_user_profile"))
        dob = request.form['dob']
        if dob:
            try:
                dob_parsed = datetime.strptime(dob, "%Y-%m-%d").date()
            except ValueError:
                flash("Invalid date of birth", "error")
                return redirect(url_for("update_user_profile"))
        else:
            dob_parsed = None
        country = request.form['country']
        if country:
            if not is_valid_country(country):
                flash("Invalid country", "error")
                return redirect(url_for("update_user_profile"))
        post_code = request.form['post_code']
        if post_code:
            if not is_valid_postal_code(post_code, country):
                print(is_valid_postal_code(post_code, country))
                flash("Invalid postal code: enter a valid country and postal code", "error")
                return redirect(url_for("update_user_profile"))
        delivery_address = request.form['delivery_address']
        if delivery_address:
            if not is_valid_address(delivery_address, post_code, country):
                flash("Invalid delivery address: enter a valid address, post code and country", "error")
                return redirect(url_for("update_user_profile"))


        user = User.query.filter_by(id=current_user.id).first()

        if user:
            user.first_name = first_name
            user.last_name = last_name
            user.gender = gender
            user.telephone = telephone
            if dob_parsed:
                user.date_of_birth = dob_parsed
            user.country = country
            user.post_code = post_code
            user.delivery_address = delivery_address

            try:
                db.session.commit()
                flash("Your profile has been successfully updated", "success")
                return redirect(url_for('user_account'))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating user profile: {str(e)}", "error")
                return redirect(url_for('update_user_profile'))
        else:
            flash("User not found", "error")
            return redirect(url_for('update_user_profile'))

    return render_template('update_user_profile.html', no_of_cartItems=no_of_cartItems, user=current_user)
