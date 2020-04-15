import unittest
from dsc.invoice import InvoiceHTMLParser


class TestInvoiceHTMLParser(unittest.TestCase):
    def test_order_id(self):
        html = """
            <html>
                <head>
                    <title>Parse it </title>
                </head>
                <body>
                    <p><strong>Date:</strong> March 14 2017 14:32:30</p>
                    <p><strong>Order ID:</strong> 890348</p>
                </body>
            </html>
        """
        parser = InvoiceHTMLParser()
        parser.feed(html)
        self.assertEqual(parser.get_order_id(), '890348')
