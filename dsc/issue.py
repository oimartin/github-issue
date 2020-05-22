import github
from dataclasses import dataclass
import mistune
import sys
import traceback
import logging


@dataclass(init=True)
class GithubIssue():
    token: str
    repository: str
    organization: str

    def __post_init__(self):

        self.connect = github.Github(self.token)

        try:
            self.repo_obj = self.connect.get_repo(
                f'{self.organization}/{self.repository}'
            )
        except (github.BadCredentialsException, github.BadAttributeException) as error:
            print(error)
            sys.exit(1)

    def issue(self, issueid: int) -> github.Issue.Issue:
        try:
            return self.repo_obj.get_issue(number=issueid)
        except github.BadAttributeException:
            sys.exit(1)

    def body(self, issueid: int) -> str:
        try:
            return self.issue(issueid).body
        except github.BadAttributeException as error:
            print(error)
            sys.exit(1)

    def html(self, issueid: int) -> str:
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
    def __init__(self, issueid, msg=None):
        if msg is None:
            msg = "An error ocurred with mistune."
        super().__init__(msg)
        self.issueid = issueid
