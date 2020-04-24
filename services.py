try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

import requests
from constants import BASE_URL

MAILGUN_URL = urljoin(BASE_URL,
                      'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org/messages')


def get_mailgun():
    response = requests.get(MAILGUN_URL)
    if response.ok:
        return response
    else:
        return None


def info():
    order = {'id': '4628',
             'user_name': 'David Knecht1',
             'shipping_email': 'oimartin1015@gmail.com',
             'trigger_label': 'Growing/InPreparation',
             'mailgun_key': 'dsdlsjflsjstandinkey13233',
             'mailgun_domain':
             'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org'}
    return order
