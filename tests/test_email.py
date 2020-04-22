import unittest
from dsc.email import send_email
from tests.dicty_order_data import info
import requests


class MailgunTestBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.order_id = info.order['id']
        self.user_name = info.order['user_name']
        self.shipping_email = info.order['shipping_email']
        self.label = info.order['trigger_label']
        self.key = info.order['mailgun_key']
        self.domain = info.order['mailgun_domain']

    def setUp(self):
        self.email = {}
        self.connect = requests.post(
            "https://api.mailgun.net/v3/" + self.domain + "/messages",
            auth=self.api_call, data=self.email)

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
