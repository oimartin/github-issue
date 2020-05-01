import requests


class EmailUser:
    """Use Mailgun API to send user order update email."""

    def __init__(self, order):
        """Initilize order information attributes."""
        self.sender = f"Excited User <postmaster@{order['mailgun_domain']}"
        self.recipient = order['shippiing_email']
        self.subject = f"DSC Order {order['id']} - {order['trigger_label']}"
        self.text = f"""Dear {order['user_name']},
                Your order status: {order['trigger_label']}
                Please let us know if you have any questions.
                Best regards,
                The DSC Team
                dictystocks@northwestern.edu"""
        self.mailgun_apicall = order.mailgun_apicall
        self.mailgun_key = order.mailgun_key

    def create_email(self):
        """Create email template to update users."""
        email = {"from": self.sender,
                 "to": self.recipient,
                 "subject": self.subject,
                 "text": self.text}
        return email

    def send_email(self):
        """Initialize email with mailgun API."""
        return requests.post(self.mailgun_apicall,
                             auth=("api", self.mailgun_key), data=self.email)
