# import dependencies
from github import Github
from config import access_token

g = Github(access_token)

repo = g.get_repo("dictybase-playground/learn-github-action")

for issue in repo.get_issues(state='open'):
    print(f"This is the first comment of {issue}: {issue.body}")
    for comment in issue.get_comments():
        print(f"These are the following comments of {issue}: {comment}")



