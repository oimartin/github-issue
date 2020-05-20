import github
from dataclasses import dataclass
import mistune
import sys


@dataclass(init=True)
class GithubIssue():
    token: str
    repository: str
    organization: str

    def __post_init__(self):

        try:
            self.connect = github.Github(self.token)
        except github.BadCredentialsException as badcred:
            print(
                f"""GitHub error status: {badcred.status}
                GitHub error data: {badcred.data}""")
            sys.exit("Check token used to connect to GitHub.")
        else:
            try:
                self.repo_obj = self.connect.get_repo(
                    f'{self.organization}/{self.repository}'
                )
            except github.BadAttributeException as badattr:
                print(
                    f"""GitHub error value: {badattr.actual_value}
                    PyGithub expected type: {badattr.expected_type}
                    PyGithb exception: {badattr.transformation_exception}""")
                sys.exit(
                    "Check the organization and repository used to connect to GitHub.")

    def issue(self, issueid: int) -> github.Issue.Issue:
        try:
            return self.repo_obj.get_issue(number=issueid)
        except github.BadAttributeException as badattr:
            print(
                f"""GitHub error value: {badattr.actual_value}
                  PyGithub expected type: {badattr.expected_type}
                  PyGithb exception: {badattr.transformation_exception}""")
            sys.exit("Could not connect to specific GitHub issue.")

    def body(self, issueid: int) -> str:
        try:
            return self.issue(issueid).body
        except github.GithubExceptions as gitexcept:
            print(
                f"""GitHub error status: {gitexcept.status}
                GitHub error data: {gitexcept.data}""")
            sys.exit("Check how connecting to issue body.")

    def html(self, issueid: int) -> str:
        try:
            self.body(issueid) == str
        except AttributeError as error:
            print(error)
            sys.exit("Issue body sent to html() function is not a string.")
        else:
            try:
                mistune.html(self.body(issueid))[:5] == '<html>'
            except MistuneError as error:
                print(error)
                sys.exit(
                    """Mistune is not creating an
                    html version of Github issue body.""")
            else:
                return mistune.html(self.body(issueid))


class MistuneError(Exception):
    def __init__(self, issueid, msg=None):
        if msg is None:
            msg = "An error ocurred with mistune."
        super().__init__(msg)
        self.issueid = issueid
