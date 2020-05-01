from dsc.cmdline import parse_cmdline
from dsc.issue import GithubIssue
from dsc.invoice import InvoiceHTMLParser
from dsc.dict import dict_order_info
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
    issue = GithubIssue(args)
    issue.github_repo()
    html = issue.mrkdwn_html()
    parser = InvoiceHTMLParser()
    parser.feed(html)
    info = dict_order_info(parser.get_all_order_info(), args)
    return EmailUser(info)


if __name__ == "__main__":
    main()
