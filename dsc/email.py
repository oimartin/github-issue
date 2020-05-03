import requests
from dsc.params import MailgunEmailParams, SendEmailParams
from dataclasses import dataclass
from string import Template


@dataclass
class EmailTemplate:
    subject_template: Template = Template('DSC Order $issue_id - $label')
    content_template: Template = Template(
                                """Dear $user,
                                Your order status: $label
                                Please let us know if you have any questions.
                                Best regards,
                                The DSC Team
                                dictystocks@northwestern.edu""")

    def generate_subject(self, issue_id: int, label: str) -> str:
        return self.subject_template.substitute(
            issue_id=issue_id,
            label=label
        )

    def generate_content(self, user: str, label: str) -> str:
        return self.content_template.substitute(
            user=user,
            label=label
        )


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
