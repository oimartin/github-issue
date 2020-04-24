from unittest.mock import Mock, patch
from services import get_mailgun, info
import unittest


class TestSendEmail(unittest.TestCase):
    def setup(self):
        self.order_id = info()['id']
        self.user_name = info()['user_name']
        self.shipping_email = info()['shipping_email']
        self.label = info()['trigger_label']
        self.key = info()['mailgun_key']
        self.domain = info()['mailgun_domain']

    @patch('services.requests.get')
    def test_get_mailgun(self, mock_get):
        mock_get.return_value.ok = True

        response = get_mailgun()

        self.assertIsNotNone(response)
