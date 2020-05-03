from github import Github, Issue, Repository
from dataclasses import dataclass
import mistune


@dataclass
class GithubIssue():
    token: str
    repository: str
    organization: str
    connect: Github(init=False)
    repo_obj: Repository(init=False)

    def __post_init__(self) -> None:
        self.connect = Github(self.token)
        self.repo_obj = self.connect.get_repo(
            f'{self.organization}/{self.repository}'
        )

    def issue(self, issueid: int) -> Issue.Issue:
        return self.repo_obj.get_issue(number=issueid)

    def body(self, issueid: int) -> str:
        return self.issue(issueid).body

    def html(self, issueid: int) -> str:
        return mistune.html(self.body(issueid))
