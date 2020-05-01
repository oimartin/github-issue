import requests


class EmailUser:
    """Use Mailgun API to send user order update email."""

    def __init__(self, order):
        """Initilize order information attributes."""
        self.mailgun_apicall = order.mailgun_apicall
        self.mailgun_key = order.mailgun_key

    def send_email(self, order):
        """Initialize email with mailgun API."""
        return requests.post(
            self.mailgun_apicall,
            auth=("api", self.mailgun_key),
            data={
                "from":
                f"Excited User <postmaster@{order.mailgun_domain}",
                "to": order.shipping_email,
                "subject": f"DSC Order {order.issue_id} - {order.trigger_label}",
                "text":
                f"""Dear {order.user_name},
                              Your order status: {order.trigger_label}
                              Please let us know if you have any questions.
                              Best regards,
                              The DSC Team
                              dictystocks@northwestern.edu"""})
