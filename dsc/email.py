import requests
import requests.exceptions
from dsc.params import SendEmailParams
from dataclasses import dataclass
from string import Template


@dataclass
class EmailTemplate:
    message: str
    subject_template: Template = Template('DSC Order $issue_id - $label')

    def __post_init__(self) -> None:
        self.content_template = Template(self.message)

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
        try:
            requests.post(
                self.endpoint,
                auth=('api', self.api_key),
                data={'from': params.sender,
                      'to': params.to,
                      'subject': params.subject,
                      'text': "Test, this is the text part.",
                      'html': params.content
                      })
        except ConnectionError as error:
            raise error
        except requests.exceptions.HTTPError as error:
            raise error
        except requests.exceptions.Timeout as error:
            raise error
        else:
            return requests.post(
                self.endpoint,
                auth=('api', self.api_key),
                data={'from': params.sender,
                      'to': 'oimartin1015@gmail.com',
                      'subject': 'Could not update user',
                      'text':
                      "Could not send an update email to user."
                      })
