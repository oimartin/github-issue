from dataclasses import dataclass


@dataclass
class GithubParams:
    token: str
    repository: str
    organization: str


@dataclass
class OrderParams:
    order_id: int
    user_name: str
    shippint_email: str
    consumer_email: str


@dataclass
class SendEmailParams:
    to: str
    sender: str
    content: str
    subject: str
