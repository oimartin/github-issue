"""Use PyGithub to connect to Github API v3."""
from dsc.cmdline import parse_cmdline
from dsc.connect import github_repo
from dsc.mrkdwn2html import issue_body, mrkdwn_html
from dsc.invoice import InvoiceHTMLParser
from dsc.dict import dict_order_info
from dsc.email import send_email


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
    repo = github_repo(args)
    mrkdwn = issue_body(args, repo)
    html = mrkdwn_html(mrkdwn)
    parser = InvoiceHTMLParser()
    parser.feed(html)
    info = dict_order_info(parser.get_all_order_info(), args)
    email_msg = send_email(info)
    return email_msg


if __name__ == "__main__":
    main()
