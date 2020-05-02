from github import Github, Issue
from dsc.params import GithubParams
import mistune


class GithubIssue():
    def __init__(self, params: GithubParams) -> None:
        self.connect = Github(params.token)
        self.repo_obj = self.connect.get_repo(
            f'{params.organization}/{params.repository}'
        )
        self.token = params.token
        self.repo = params.repository
        self.organization = params.organization

    def issue(self, issueid: int) -> Issue.Issue:
        return self.repo_obj.get_issue(number=issueid)

    def body(self, issueid: int) -> str:
        return self.issue(issueid).body

    def html(self, issueid: int) -> str:
        return mistune.html(self.body(issueid))
