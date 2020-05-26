import github
from dataclasses import dataclass
import mistune


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
        except github.BadCredentialsException as badcred:
            raise badcred

        except github.BadAttributeException as badattr:
            raise badattr

    def issue(self, issueid: int) -> github.Issue.Issue:
        """Get Github issue.

        Arguments:
            issueid {int} -- [Github Issue Id number]

        Returns:
            github.Issue.Issue -- [Specific Github issue]
        """
        try:
            return self.repo_obj.get_issue(number=issueid)
        except github.BadAttributeException as badattr:
            raise badattr

    def body(self, issueid: int) -> str:
        """Get the body of the specific issue.

        Arguments:
            issueid {int} -- [Specific Github issue]

        Returns:
            str -- [markdown of issue body]
        """
        try:
            return self.issue(issueid).body
        except github.BadAttributeException as badattr:
            raise badattr

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
            raise error
        else:
            try:
                mistune.html(self.body(issueid))[0] == '<'
            except MistuneError as error:
                raise error
            else:
                return mistune.html(self.body(issueid))

    def comment_status(self, issueid: int, message: str) -> github.IssueComment.IssueComment:
        return self.issue(issueid).create_comment(message)

    def remove_label(self, issueid: int, label: str) -> github.Label.Label:
        return self.issue(issueid).remove_from_labels(label)


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
