import requests
from dsc.params import SendEmailParams
from dataclasses import dataclass
from string import Template


@dataclass
class EmailTemplate:
    subject_template: Template = Template('DSC Order $order_id - $label')
    content_template: Template = Template(
                                """Dear $user,
                                Your order status: $label
                                Please let us know if you have any questions.
                                Best regards,
                                The DSC Team
                                dictystocks@northwestern.edu""")

    def generate_subject(self, order_id: int, label: str) -> str:
        return self.subject_template.substitute(
            issue_id=order_id,
            label=label
        )

    def generate_content(self, user: str, label: str) -> str:
        return self.content_template.substitute(
            user=user,
            label=label
        )


@dataclass
class Email:
    """Use Mailgun API to send user order update email."""
    endpoint: str
    api_key: str

    def send(self, params: SendEmailParams) -> None:
        """send email with mailgun API."""
        return requests.post(
            self.endpoint,
            auth=('api', self.api_key),
            data={'from': params.sender,
                  'to': params.to,
                  'subject': params.subject,
                  'text': params.content
                  })
