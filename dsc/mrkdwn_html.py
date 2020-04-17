"""Markdown to html."""
import mistune
import connect_repo
import cmdline_arg


def get_issue_body():
    """Get issue/order of interest.

    Arguments:
        repo  -- connect to repo
        id int -- issue/order id

    Returns:
        issue -- markdown of issue body

    """
    issue_id = cmdline_arg.parse_cmdline().args.id
    issue = connect_repo.github_repo.get_issue(number=issue_id)

    return issue


def mrkdwn_html(issue):
    """Convert issue body to html.

    Arguments:
        issue str -- the entire issue/order

    Returns:
        issue_body_html -- in html format

    """
    issue_body = issue.body
    issue_body_html = mistune.html(issue_body)

    return issue_body_html
