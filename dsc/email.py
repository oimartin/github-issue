import requests
from dsc.params import SendEmailParams
from dataclasses import dataclass
from string import Template
from style.style import send_style
from style.message import send_body


@dataclass
class EmailTemplate:
    subject_template: Template = Template('DSC Order $issue_id - $label')
    content_template: Template = Template(
        f"""
<html>
    {send_style()}
            {send_body()}
</html>
        """)

    def generate_subject(self, issue_id: int, label: str) -> str:
        return self.subject_template.substitute(
            issue_id=issue_id,
            label=label
        )

    def generate_content(self, user: str, label: str, issue_id: int) -> str:
        return self.content_template.substitute(
            user=user,
            label=label,
            issue_id=issue_id
        )


@dataclass
class Email:
    """Use Mailgun API to send user order update email."""

    endpoint: str
    api_key: str

    def send(self, params: SendEmailParams) -> None:
        """Send email with mailgun API."""
        with open("style/html_email.html", 'w') as f:
            f.write(params.content)
        return requests.post(
            self.endpoint,
            auth=('api', self.api_key),
            data={'from': params.sender,
                  'to': params.to,
                  'subject': params.subject,
                  'text': "Test, this is the text part.",
                  'html': params.content
                  })
