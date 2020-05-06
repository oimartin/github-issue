import unittest
from dsc.legacyinvoice import InvoiceHTMLParser
import os
from collections import namedtuple

TEST_FOLDER = os.path.join(os.path.dirname(__file__))


class TestInvoiceHTMLParser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        input = os.path.join(TEST_FOLDER, 'legacy_invoice_data.html')
        with open(input, 'r') as f:
            cls.html = f.read()

    def setUp(self):
        self.parser = InvoiceHTMLParser()
        self.parser.feed(self.html)

    def test_order_id(self):
        self.assertEqual(
            self.parser.get_order_id(),
            '9277')

    def test_shipping_email(self):
        self.assertEqual(
            self.parser.get_shipping_email(),
            'rrijal@bio.tamu.edu')

    def test_user_name(self):
        self.assertEqual(
            self.parser.get_user_name(),
            'Ramesh Rijal')

    def test_all_order_info(self):
        OrderParams = namedtuple('OrderParams',
                                 ['order_id', 'user_name',
                                  'shipping_email', 'consumer_email'])
        self.assertTupleEqual(
            self.parser.get_all_order_info(),
            OrderParams(order_id='9277', user_name='Ramesh Rijal',
                        shipping_email='rrijal@bio.tamu.edu',
                        consumer_email=''))

    def test_all(self):
        self.assertEqual(
            self.parser.get_order_id(),
            '9277')
        self.assertEqual(
            self.parser.get_shipping_email(),
            'rrijal@bio.tamu.edu')
        self.assertEqual(
            self.parser.get_user_name(),
            'Ramesh Rijal')
