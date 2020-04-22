"""Dictionary order data."""
from config import key


def info():
    order = {'id': '4628',
             'user_name': 'David Knecht1',
             'shipping_email': 'oimartin1015@gmail.com',
             'trigger_label': 'Growing/InPreparation',
             'mailgun_key': key,
             'mailgun_domain': 'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org'}
    return order['id'], order['user_name'], order['shipping_email'], order['trigger_label'], order['mailgun_key'], order['mailgun_domain']
