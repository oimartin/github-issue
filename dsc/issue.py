from github import Github
from collections import namedtuple
import mistune

GithubParams = namedtuple('GithubParams',
                          ['token',
                           'repository',
                           'organization'
                           ])


class GithubIssue():
    """Connect to GitHub repo and return html of issue body.

    Arguments:
        Github {class} -- Bridge to GitHub API
    """

    def __init__(self, info):
        """Initialize commandline attributes."""
        self.body = ''
        self.connect = Github(info.token).get_repo(
            f'{info.organization}/{info.repository}')

    def get_body(self, issueid):
        """Generate html versision of issue body."""
        self.body = self.connect.get_issue(number=issueid).body
        return self.body

    def mrkdwn_html(self):
        """Generate html versision of issue body."""
        return mistune.html(self.body)
