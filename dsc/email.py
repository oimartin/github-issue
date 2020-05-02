import requests
from dsc.params import MailgunEmailParams, SendEmailParams


class Email:
    """Use Mailgun API to send user order update email."""

    def __init__(self, params: MailgunEmailParams) -> None:
        """Initilize order information attributes."""
        self.endpoint = params.endpoint
        self.api_key = params.api_key

    def send(self, params: SendEmailParams) -> None:
        """send email with mailgun API."""
        return requests.post(
            self.endpoint,
            auth=('api', self.api_key),
            data={'from': params.send,
                  'to': params.to,
                  'subject': params.subject,
                  'text': params.content
                  })
                  
                "from":
                f"Excited User <postmaster@{order.mailgun_domain}",
                "to": order.shipping_email,
                "subject": f"DSC Order {order.issue_id} - {order.trigger_label}",
                "text":



                            """Dear {order.user_name},
                              Your order status: {order.trigger_label}
                              Please let us know if you have any questions.
                              Best regards,
                              The DSC Team
                              dictystocks@northwestern.edu"""}
