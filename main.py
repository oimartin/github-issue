from dsc.cmdline import parse_cmdline
from dsc.githubrepo import github
from dsc.issue import GithubIssue
from dsc.invoice import InvoiceHTMLParser
from dsc.orderinfo import order_info
from dsc.useremail import EmailUser


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
    connected = github(args)
    issue = GithubIssue(connected)
    issue.get_body(args.issueid)
    html = issue.mrkdwn_html()
    parser = InvoiceHTMLParser()
    parser.feed(html)
    info = order_info(parser.get_all_order_info(), args)
    details = EmailUser(info)
    return details.send_email(info)


if __name__ == "__main__":
    main()
