from html.parser import HTMLParser
from dsc.params import OrderInfo


class InvoiceHTMLParser(HTMLParser):
    """Grab info from html version of issue body.

    Arguments:
        HTMLParser {class}
    """

    def __init__(self) -> None:
        """Initialize attributs."""
        self._nth_td_tag = 0
        self._nth_br_tag = 0
        self.nth_strong_tag = 0
        self._shipto_email = ''
        self._consumer_email = ''
        self.order_id = ''
        self._user_name = ''
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs) -> None:
        """Manage <td> html elements."""
        if tag == 'td':
            self._nth_td_tag += 1

    def handle_endtag(self, tag) -> None:
        """Manage <strong> html elements."""
        if tag == 'strong':
            self.nth_strong_tag += 1

    def handle_startendtag(self, tag, attrs) -> None:
        """Manage <br> html elements."""
        if tag == 'br':
            if self._nth_td_tag >= 2:
                self._nth_br_tag += 1

    def handle_data(self, data) -> None:
        """Count number of html elements."""
        if self.nth_strong_tag == 2:
            if not self.order_id:
                self.order_id = data
        if self._nth_td_tag == 2:
            if not self._user_name:
                self._user_name = data
        if self._nth_br_tag == 8:
            if not self._shipto_email:
                self._shipto_email = data
        if self._nth_br_tag == 17:
            if not self._consumer_email:
                self._consumer_email = data

    def get_order_id(self) -> str:
        """Retrieve order id."""
        return self.order_id.strip()

    def get_user_name(self) -> str:
        """Retrieve user shipping name."""
        return self._user_name.strip()

    def get_shipping_email(self) -> str:
        """Retrieve shipping email."""
        return self._shipto_email.strip()

    def get_consumer_email(self) -> str:
        """Retrieve consumer email."""
        return self._consumer_email.strip()

    def get_all_order_info(self) -> OrderInfo:
        """Retrieve all info for order."""
        return OrderInfo(order_id=self.order_id.strip(),
                         user_name=self._user_name.strip(),
                         shipping_email=self._shipto_email.strip(),
                         consumer_email=self._consumer_email.strip())
