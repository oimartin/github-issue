from unittest.mock import patch
from services import get_mailgun, info, get_update_email
import unittest


class TestSendEmail(unittest.TestCase):
    def setup(self):
        self.email = info()

    @patch('services.requests.get')
    def test_get_mailgun_ok(self, mock_get):
        mock_get.return_value.ok = True

        response = get_mailgun()

        self.assertIsNotNone(response)

    @patch('services.requests.get')
    def test_get_mailgun_not_ok(self, mock_get):
        mock_get.return_value.ok = False

        response = get_mailgun()

        self.assertIsNotNone(response)

    @patch('services.requests.post')
    def test_update_email(self, mock_get):
        mock_get.return_value.ok = True

        response = get_update_email(info())

        self.assertIsNotNone(response)
