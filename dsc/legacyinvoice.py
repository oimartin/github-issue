from html.parser import HTMLParser
from dsc.params import OrderInfo


class InvoiceHTMLParser(HTMLParser):
    """Grab info from html version of legacy issue body.
    There is no consumer email in legacy order.

    Arguments:
        HTMLParser {class}
    """

    def __init__(self) -> None:
        """Initialize attributs."""
        self._nth_p_tag = 0
        self._nth_h1_tag = 0
        self.nth_strong_tag = 0
        self._shipto_email = ''
        self._consumer_email = ''
        self.order_id = ''
        self._user_name = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs) -> None:
        """Manage <p> html elements."""
        if tag == 'p':
            self._nth_p_tag += 1

    def handle_endtag(self, tag) -> None:
        """Manage <strong> html elements."""
        if tag == 'strong':
            self.nth_strong_tag += 1

    def handle_data(self, data) -> None:
        """Count number of html elements."""
        if self.nth_strong_tag == 3:
            if not self.order_id:
                self.order_id = data[2:]
        if self._nth_p_tag == 2:
            if not self._user_name:
                self._user_name = data.split("\n")[0]
        if self.nth_strong_tag == 2:
            if not self._shipto_email:
                self._shipto_email = data[2:]

    def get_order_id(self) -> str:
        """Retrieve order id."""
        return self.order_id.strip()

    def get_user_name(self) -> str:
        """Retrieve user shipping name."""
        return self._user_name.strip()

    def get_shipping_email(self) -> str:
        """Retrieve shipping email."""
        return self._shipto_email.strip()

    def get_all_order_info(self) -> OrderInfo:
        """Retrieve all info for order."""
        return OrderInfo(order_id=self.order_id.strip(),
                         user_name=self._user_name.strip(),
                         shipping_email=self._shipto_email.strip(),
                         consumer_email=self._consumer_email.strip())
