from github import Github, Issue
from dataclasses import dataclass
import mistune
import sys


@dataclass(init=True)
class GithubIssue():
    token: str
    repository: str
    organization: str

    def __post_init__(self) -> None:
        try:
            self.connect = Github(self.token)
            self.repo_obj = self.connect.get_repo(
                f'{self.organization}/{self.repository}'
            )
        except AssertionError as error:
            print(error)
            sys.exit("Check provided token, repository, and organization.")

    def issue(self, issueid: int) -> Issue.Issue:
        try:
            return self.repo_obj.get_issue(number=issueid)
        except IssueIdError as error:
            print(error)
            sys.exit("Could not connect to specific GitHub issue.")

    def body(self, issueid: int) -> str:
        return self.issue(issueid).body

    def html(self, issueid: int) -> str:
        return mistune.html(self.body(issueid))


class IssueIdError(Exception):
    def __init__(self, issueid, msg=None):
        if msg is None:
            msg = "An error occured with the issue id."
        super().__init__(msg)
        self.issueid = issueid
