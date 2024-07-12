from flask import session, redirect, url_for, render_template, flash
from flask_login import login_required, current_user
from db import db
from models.orders import Order
from models.orderitem import OrderItem
import paypalrestsdk
import uuid
from models.products import Product
from dotenv import load_dotenv
import os

load_dotenv() 

@login_required
def pay():
    cart = session.get('cart', {})
    user = current_user
    if not user.country or not user.post_code or not user.delivery_address:
        flash('please fill up your address', 'error')
        return redirect(url_for('update_user_profile'))

    if not cart or not user:
        return "No items in cart or user not logged in"

    cart_items = []
    for key, value in cart.items():
        product = Product.query.filter_by(id=uuid.UUID(key)).first()
        if product:
            item = {
                'product_id': key,
                'name': product.name,
                'price': product.final_price,
                'quantity': value
            }
            cart_items.append(item)

    total_amount = sum(item['price'] * item['quantity'] for item in cart_items)
    user_id = user.id

    order = Order(user_id=user_id, total_amount=total_amount, currency='USD')
    db.session.add(order)
    db.session.commit()

    for item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            price=item['price']   
        )
        db.session.add(order_item)
    db.session.commit()

    paypalrestsdk.configure({
    "mode": 'sandbox',
    "client_id":os.environ.get('PAYPAL_CLIENT_ID'),
    "client_secret": os.environ.get('PAYPAL_CLIENT_SECRET')
    })

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('execute_payment', order_id=order.id, _external=True),
            "cancel_url": url_for('payment_cancel', order_id=order.id, _external=True)
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": item['name'],
                    "sku": str(item['product_id']),
                    "price": "{:.2f}".format(item['price']),
                    "currency": order.currency,
                    "quantity": item['quantity']
                } for item in cart_items]
            },
            "amount": {
                "total": "{:.2f}".format(order.total_amount),
                "currency": order.currency
            },
            "description": f"Order #{order.id}"
        }]
    })

    if payment.create():
        order.payment_id = payment.id
        db.session.commit()
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return redirect(approval_url)
    else:
        return render_template('payment_failure.html', error=payment.error)

