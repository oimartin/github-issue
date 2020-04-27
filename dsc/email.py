
"""Send user update email."""
import requests
label = 'Growing/In Preparation'


def send_email(order):
    """Create email template to update users."""
    email = {"from": "Excited User <postmaster@" + order['mailgun_domain'],
             "to": order['shipping_email'],
             "subject": f"DSC Order {order['id']} - {order['trigger_label']}",
             "text": f"""Dear {order['user_name']},
              Your order status: {order['trigger_label']}
              Please let us know if you have any questions.
              Best regards,
              The DSC Team
              dictystocks@northwestern.edu"""}

    return requests.post(order['mailgun_apicall'],
                         auth=("api", order['mailgun_key']), data=email)
