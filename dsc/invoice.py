from html.parser import HTMLParser


class InvoiceHTMLParser(HTMLParser):
    def __init__(self):
        self.nth_strong_tag = 0
        self.order_id = ''

    def handle_endtag(self, tag):
        if tag == 'strong':
            self.nth_strong_tag += 1

    def handle_data(self, data):
        if self.nth_strong_tag == 2:
            self.order_id = data

    def order_id(self):
        return self.order_id.lstrip()
