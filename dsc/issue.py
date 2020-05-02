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

    def __init__(self, params):
        """Initialize commandline attributes."""
        self.token = params.token
        self.repository = params.repository
        self.organization = params.organization
        self.connect = Github(params.token)

    def repo(self):
        """Returns a repository object
        """
        return self.connect.get_repo(f'{self.organization}/{self.repository}')

    def body(self, issueid):
        """Gets raw markdown content of issue body."""
        return self.repo().get_issue(number=issueid).body

    def html(self, issueid):
        """Generate html versision of issue body."""
        return mistune.html(self.body(issueid))
