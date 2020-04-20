"""Use PyGithub to connect to Github API v3."""
from dsc.cmdline import parse_cmdline
from dsc.connect import github_repo
from dsc.mrkdwn2html import issue_body, mrkdwn_html
from dsc.invoice import InvoiceHTMLParser
from dsc.dict import dict_order_info
from dsc.email import send_email
from config import key


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
    order = dict_order_info(parser.get_order_id(), parser.get_user_name(),
                            parser.get_shipping_email(), args.label)
    email_msg = send_email(order['id'], order['user_name'],
                           order['shipping_email'],
                           order['trigger_label'], key)
    return email_msg


if __name__ == "__main__":
    main()
