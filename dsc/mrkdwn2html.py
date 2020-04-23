"""Markdown to html."""
import mistune


def issue_body(repo, id):
    """Get issue/order of interest.

    Arguments:
        repo  -- connect to repo
        id int -- issue/order id

    Returns:
        issue -- markdown content of issue body

    """
    return repo.get_issue(number=id[2]).body


def mrkdwn_html(body):
    """Convert issue body to html.

    Arguments:
        body -- the markdown content of issue body

    Returns:
        issue_body_html -- in html format

    """
    return mistune.html(body)
