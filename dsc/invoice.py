"""Parse html to get emails and order id data."""
from html.parser import HTMLParser


class InvoiceHTMLParser(HTMLParser):
    def __init__(self):

        self._nth_td_tag = 0
        self._nth_br_tag = 0
        self.nth_strong_tag = 0
        self._shipto_email = ''
        self._consumer_email = ''
        self.order_id = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        """Manage <td> html elements."""
        if tag == 'td':
            self._nth_td_tag += 1

    def handle_endtag(self, tag):
        """Manage <strong> html elements."""
        if tag == 'strong':
            self.nth_strong_tag += 1

    def handle_startendtag(self, tag, attrs):
        """Manage <br> html elements."""
        if tag == 'br':
            if self._nth_td_tag >= 2:
                self._nth_br_tag += 1

    def handle_data(self, data):
        """Count number of html elements."""
        if self.nth_strong_tag == 2:
            if not self.order_id:
                self.order_id = data
        if self._nth_br_tag == 8:
            if not self._shipto_email:
                self._shipto_email = data
        if self._nth_br_tag == 17:
            if not self._consumer_email:
                self._consumer_email = data

    def get_order_id(self):
        """Retrieve order id."""
        return self.order_id.strip()

    def get_shipping_email(self):
        """Retrieve shipping email."""
        return self._shipto_email.strip()

    def get_consumer_email(self):
        """Retrieve consumer email."""
        return self._consumer_email.strip()
