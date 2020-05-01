from github import Github
import mistune


class GithubIssue(Github):
    """Connect to GitHub repo and return html of issue body.

    Arguments:
        Github {class} -- Bridge to GitHub API
    """

    def __init__(self, cmdline):
        """Initialize commandline attributes."""
        self.token = cmdline.token
        self.organization = cmdline.organization
        self.repository = cmdline.repository
        self.issueid = cmdline.issueid
        self.connect = ''
        self.body = ''

    def github_repo(self):
        """Prepare connection to repository."""
        self.connect = Github(self.token).get_repo(f'{self.organization}/{self.repository}')
        self.body = self.connect.get_issue(number=self.issueid).body
        return self.body

    def mrkdwn_html(self):
        """Generate html versision of issue body."""
        return mistune.html(self.body)
