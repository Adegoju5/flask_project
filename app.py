# flask_project/app.py
from flask import Flask
from db import db 
import logging

app = Flask(__name__)

app.secret_key = 'Fabregas_3015$'

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://debowalealex:Fabregas_3015$@localhost:5432/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

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
from routes.product_route import product
from routes.cart_route import cart

# Register routes
app.add_url_rule('/home', view_func=home)
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/product_add', view_func=add_product, methods=['GET', 'POST'])
app.add_url_rule('/categories', view_func=categories, methods=['GET', 'POST'])
app.add_url_rule('/products/<argument>', view_func=products, methods=['GET'])
app.add_url_rule('/product', view_func=product, methods=['GET'])
app.add_url_rule('/about', view_func=about, methods=['GET'])
app.add_url_rule('/', view_func=landing_page, methods=['GET'])
app.add_url_rule('/discounts', view_func=discounts, methods=['GET'])
app.add_url_rule('/account', view_func=user_account, methods=['GET'])
app.add_url_rule('/cart', view_func=cart, methods=['GET'])



if __name__ == '__main__':
    app.run(debug=True)

