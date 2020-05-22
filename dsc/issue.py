import github
from dataclasses import dataclass
import mistune
import sys


@dataclass(init=True)
class GithubIssue():
    """Connect to Github API and return html version of issue body."""

    token: str
    repository: str
    organization: str

    def __post_init__(self):
        """Take in Github token, repo and org."""
        self.connect = github.Github(self.token)

        try:
            self.repo_obj = self.connect.get_repo(
                f'{self.organization}/{self.repository}'
            )
        except (github.BadCredentialsException,
                github.BadAttributeException) as error:
            print(error)
            sys.exit(1)

    def issue(self, issueid: int) -> github.Issue.Issue:
        """Get Github issue.

        Arguments:
            issueid {int} -- [Github Issue Id number]

        Returns:
            github.Issue.Issue -- [Specific Github issue]
        """
        try:
            return self.repo_obj.get_issue(number=issueid)
        except github.BadAttributeException:
            sys.exit(1)

    def body(self, issueid: int) -> str:
        """Get the body of the specific issue.

        Arguments:
            issueid {int} -- [Specific Github issue]

        Returns:
            str -- [markdown of issue body]
        """
        try:
            return self.issue(issueid).body
        except github.BadAttributeException as error:
            print(error)
            sys.exit(1)

    def html(self, issueid: int) -> str:
        """Create html string of specific issue body.

        Arguments:
            issueid {int} -- [Specific Github issue]

        Returns:
            str -- [html version of issue body]
        """
        try:
            self.body(issueid) == str
        except AttributeError as error:
            print(error)
            sys.exit(1)
        else:
            try:
                mistune.html(self.body(issueid))[:5] == '<html>'
            except MistuneError as error:
                print(error)
                sys.exit(1)
            else:
                return mistune.html(self.body(issueid))


class MistuneError(Exception):
    """Create error to catch if mistune mod does not work.

    Arguments:
        Exception {class} -- [-]
    """

    def __init__(self, issueid, msg=None):
        if msg is None:
            msg = "An error ocurred with mistune."
        super().__init__(msg)
        self.issueid = issueid
