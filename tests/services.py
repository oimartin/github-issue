from urllib.parse import urljoin
import requests

BASE_URL = 'https://api.mailgun.net/v3/'

MAILGUN_URL = urljoin(BASE_URL,
    'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org/messages')


def get_mailgun():
    response = requests.get(MAILGUN_URL)
    if response.ok:
        return response
    else:
        return None


def info():
    email = {"from": "Excited User <postmaster@,sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org",
             "to": 'david.knecht@uconn.edu',
             "subject": 'DSC Order 890348 - Growing/InPreparation',
             "text": f"""Dear David Knecht1,
             Your order status: Growing/InPreparation
             Please let us know if you have any questions.
             Best regards,
             The DSC Team
             dictystocks@northwestern.edu"""}
    return email


def get_update_email(email):
    response = requests.post(MAILGUN_URL,
                             auth=("api", 'dsdlsjflsjstandinkey13233'),
                             data=email)

    if response.ok:
        return response
    else:
        return None
