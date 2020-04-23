"""Teset sendemail() module, mailgun API."""
import unittest
from dsc.email import send_email
from orderdata import info
import requests


class MailgunTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.order_id = info()['id']
        cls.user_name = info()['user_name']
        cls.shipping_email = info()['shipping_email']
        cls.label = info()['trigger_label']
        cls.key = info()['mailgun_key']
        cls.domain = info()['mailgun_domain']

    def setUp(self):
        self.email = {}
        self.connect = requests.post(
            "https://api.mailgun.net/v3/" + self.domain + "/messages",
            auth=("api", self.key), data=self.email)

    def test_connect(self):
        self.assertEqual(
            self.connect.status_code, '200')

    def test_email(self):
        self.email = send_email(
            self.order_id, self.user_name, self.shipping_email, self.label,
            self.key, self.domain)

        self.assertEqual(
            self.email,
            {"from": "Excited User <postmaster@" +
             'sandboxe866881ecbfb41dfb4edf4dc44fbc482.mailgun.org',
             "to": 'oimartin1015@gmail.com',
             "subject": 'DSC Order 4628 - Growing/InPreparation',
             "text": f"""Dear David Knecht1,
              Your order status: Growing/InPreparation
              Please let us know if you have any questions.
              Best regards,
              The DSC Team
              dictystocks@northwestern.edu"""}
        )

    def test_all(self):
        self.email = send_email(
            self.order_id, self.user_name, self.shipping_email, self.label,
            self.key, self.domain)

        self.assertEqual(
            self.connect.status_code, '200'
        )
