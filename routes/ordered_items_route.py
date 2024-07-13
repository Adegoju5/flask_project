from flask import render_template, session
from models.products import Product
from models.orderitem import OrderItem
from models.orders import Order
from models.users_model import User
from flask_login import current_user, login_required
from datetime import datetime
from sqlalchemy import cast, String

@login_required
def ordered_items():
    user_id = str(current_user.id)
    try:
        orders = Order.query.filter(cast(Order.user_id, String) == user_id, Order.status == 'Completed').all()
    except:
        orders=[]
    
    all_orders = []
    try:
        for order in orders:
            order_items = OrderItem.query.filter_by(order_id=order.id).all()
            for item in order_items:
                product = Product.query.filter_by(id=item.product_id).first()
                item.ordered_date = order.created_at.strftime('%Y-%m-%d')
                item.product_name = product.name
                item.size = product.size
                item.image_path = product.image_path
                all_orders.append(item)
    except:
        all_orders=[]

    sorted_orders = sorted(all_orders, key=lambda item: item.ordered_date)
    print(sorted_orders)           
    total = session.get('total', {})
    no_of_cartItems = total.get('no_of_items', 0)
    no_of_cartItems = no_of_cartItems if no_of_cartItems else ''
    return render_template('ordered_products.html', orders=sorted_orders, no_of_cartItems=no_of_cartItems)
