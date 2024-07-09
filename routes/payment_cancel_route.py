from flask import render_template
from flask_login import login_required
from models.orders import Order
from db import db



@login_required
def payment_cancel(order_id):
    order = Order.query.get_or_404(order_id)
    order.status = 'Cancelled'
    db.session.commit()
    return render_template('payment_failure.html')