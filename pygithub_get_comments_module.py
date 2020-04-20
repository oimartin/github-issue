"""Use PyGithub to connect to Github API v3."""
from dsc.cmdline import parse_cmdline
from dsc.connect import github_repo
from dsc.mrkdwn2html import issue_body, mrkdwn_html
from dsc.invoice import InvoiceHTMLParser


def main():
    """Execute other functions in script.

    Executes:
        parse_cmdline() -- command-line interface
        github_repo -- connect to org/repo
        issue_comments -- output issue content
    Returns:
        order_info -- order id, shipping and consumer emails
    """
    args = parse_cmdline()
    repo = github_repo(args.token, args.organization, args.repository)
    mrkdwn = issue_body(repo, args.issue_id)
    html = mrkdwn_html(mrkdwn)
    parser = InvoiceHTMLParser()
    parser.feed(html)

    order_info = {'order_id': parser.get_order_id(),
                  'user_name': parser.get_user_name(),
                  'shipping_email': parser.get_shipping_email(),
                  'consumer_email': parser.get_consumer_email()}
    print(order_info)
    return order_info


if __name__ == "__main__":
    main()
