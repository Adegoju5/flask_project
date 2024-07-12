from flask import request, render_template, session
from models.orders import Order
from db import db
from flask_login import login_required
import paypalrestsdk
from email_utils import send_manual_order_complete_email



@login_required
def execute_payment(order_id):
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        try:
            session['cart']={}
            order = Order.query.get_or_404(order_id)
            order.status = 'Completed'
            db.session.commit()
            return render_template('payment_successful.html')
        except Exception as e:
            send_manual_order_complete_email(payment_id)
            db.session.rollback()
            return render_template('payment_successful.html')
    else:
        return render_template('payment_failure.html')