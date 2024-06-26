# flask_project/app.py
from flask import Flask
from db import db 
import logging
from extensions import login_manager
from models.users_model import User
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'Fabregas_3015$'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://debowalealex:Fabregas_3015$@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

# Initialize the database
db.init_app(app)
login_manager.init_app(app)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Import routes (import after db is initialized to avoid circular imports)
from routes.home_route import home
from routes.login_route import login
from routes.register_route import register
from routes.product_add import add_product
from routes.categories_route import categories
from routes.products_route import products
from routes.about_route import about
from routes.landing_page_route import landing_page
from routes.discounts_route import discounts
from routes.user_account_route import user_account
from routes.change_product_route import change_product
from routes.cart_route import cart
from routes.add_to_cartItem_route import add_to_cartItem
from routes.substract_from_cartItem_route import substract_from_cartItem
from routes.remove_from_cartItem import remove_from_cartItem
from routes.logout_route import logout

# Register routes
app.add_url_rule('/home', view_func=home)
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/product_add', view_func=add_product, methods=['GET', 'POST'])
app.add_url_rule('/categories', view_func=categories, methods=['GET', 'POST'])
app.add_url_rule('/products/<argument>', view_func=products, methods=['GET'])
app.add_url_rule('/change_product', view_func=change_product, methods=['GET'])
app.add_url_rule('/about', view_func=about, methods=['GET'])
app.add_url_rule('/', view_func=landing_page, methods=['GET'])
app.add_url_rule('/discounts', view_func=discounts, methods=['GET'])
app.add_url_rule('/account', view_func=user_account, methods=['GET'])
app.add_url_rule('/cart', view_func=cart, methods=['GET'])
app.add_url_rule('/add_to_cartItem/<product_id>', view_func=add_to_cartItem, methods=['GET'])
app.add_url_rule('/substract_from_cartItem/<product_id>', view_func=substract_from_cartItem, methods=['GET'])
app.add_url_rule('/remove_from_cartItem/<product_id>', view_func=remove_from_cartItem, methods=['GET'])

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

if __name__ == '__main__':
    app.run(debug=True)

