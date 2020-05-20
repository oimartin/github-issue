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
        return self.issue(issueid).body

    def html(self, issueid: int) -> str:
        return mistune.html(self.body(issueid))
