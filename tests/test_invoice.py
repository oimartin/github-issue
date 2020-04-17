"""Parse html."""
import unittest
from dsc.invoice import InvoiceHTMLParser
import dsc.mrkdwn_html


class TestInvoiceHTMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mrkdwn_html.mrkdwn_html()

    def setUp(self):
        """Parse html."""
        self.parser = InvoiceHTMLParser()
        self.parser.feed(self.html)

    def test_order_id(self):
        """Unit test."""
        self.assertEqual(self.parser.get_order_id(), '890348')

    def test_shipping_email(self):
        """Unit test."""
        self.assertEqual(
            self.parser.shipping_email(),
            'david.knecht@uconn.edu')

    def test_consumer_email(self):
        """Unit test."""
        self.assertEqual(
            self.parser.consumer_email(),
            'abc@abc.edu')
