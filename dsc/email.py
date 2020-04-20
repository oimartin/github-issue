
"""Send user update email."""
import requests
label = 'Growing/In Preparation'


def send_email(order_id, user_name, shipping_email, label, key):
    print(f"order id - {order_id}")
    print(f"user name - {user_name}")
    print(f"shipping email - {shipping_email}")
    print(f"label - {label}")

    domain = 'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org'

    email = {"from": "Excited User mailgun@" + domain,
             "to": [shipping_email, "mailgun@" + domain],
             "subject": f"DSC Order {order_id} - {label}",
             "text": f"""Dear {user_name},
              Your order status: {label}
              Please let us know if you have any questions.
              Best regards,
              The DSC Team
              dictystocks@northwestern.edu"""}
    print(email)
    api_call = "https://api.mailgun.net/v3/" + domain + "/messages"
    return requests.post(api_call, auth=("api", key), data=email)
