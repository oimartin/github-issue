
"""Send user update email."""
import requests
label = 'Growing/In Preparation'


def send_email(order_id, user_name, shipping_email, label, key, domain):

    email = {"from": "Excited User <postmaster@" + domain,
             "to": [shipping_email],
             "subject": f"DSC Order {order_id} - {label}",
             "text": f"""Dear {user_name},
              Your order status: {label}
              Please let us know if you have any questions.
              Best regards,
              The DSC Team
              dictystocks@northwestern.edu"""}

    api_call = "https://api.mailgun.net/v3/" + domain + "/messages"
    return requests.post(api_call, auth=("api", key), data=email)
