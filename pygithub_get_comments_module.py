"""Use PyGithub to connect to Github API v3."""
import dsc.cmdline_arg
import dsc.connect_repo
import dsc.mrkdwn_html
from tests.test_invoice import TestInvoiceHTMLParser


def main():
    """Execute other functions in script.

    Executes:
        parse_cmdline() -- command-line interface
        github_repo -- connect to org/repo
        issue_comments -- output issue content
    """
    args = cmdline_arg.parse_cmdline()
    repo = connect_repo.github_repo(args)
    html = mrkdwn_html.get_issue_body(repo, args.issue_id)
    TestInvoiceHTMLParser(html)


def test_all_output():
    """Test suite - grabbing info from html."""
    suite = unittest.TestSuite()
    suite.addTest(TestInvoiceHTMLParser('test_order_id'))
    suite.addTest(TestInvoiceHTMLParser('shipping_email'))
    suite.addTest(TestInvoiceHTMLParser('test_consumer_email'))
    return suite


if __name__ == "__main__":
    main()
    runner = unittest.TextTestRunner()
    runner.run(suite())
