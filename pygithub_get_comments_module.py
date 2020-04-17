"""Use PyGithub to connect to Github API v3."""
import cmdline_arg
import connect_repo
import mrkdwn_html
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


if __name__ == "__main__":
    main()
