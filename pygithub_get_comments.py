# import dependencies
from github import Github
from config import access_token
import re

# Connect to learn-github-action repo
connect = Github(access_token)
learn_github_action = connect.get_repo("dictybase-playground/learn-github-action")

# Loop through all issues
for issue in learn_github_action.get_issues(state='open'):
    
    # See if issue body has an @ to find ean email
    if '@' in issue.body:

        # Find emails and store in list
        emails = re.findall('\S+@\S+', issue.body)
        print(f"This is an email/s, {emails}, for issue id: {issue.id}")

    # Print just the issue id and body of first comment
        print(f"This is the first comment of {issue.id}: {issue.body}")

    # Loop through all comments of specific issue
    for comment in issue.get_comments():

        # Print issue id, comment id, and the following comments
        print(f"These are the following comments of {issue.id}: {comment.id} - {comment.body}")



