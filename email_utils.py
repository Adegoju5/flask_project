from flask_mail import Message
from flask import url_for
from extensions import mail
from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def get_reset_token(user_id, expires_sec=1800):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps(str(user_id), salt='reset-password')



def verify_reset_token(token):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token, salt='reset-password', max_age=1800)
    except:
        return None
    return user_id



def send_reset_email(user):
    token = get_reset_token(user_id=user.id, expires_sec=1800)
    msg = Message('Password Reset Request',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)



def send_manual_order_complete_email(payment_id):
    msg = Message('Manual Order Complete Request',
                  recipients=['adegojualexander@gmail.com'])
    msg.body = f''' please manually set the order with the payment id {payment_id} to completed
'''
    mail.send(msg)