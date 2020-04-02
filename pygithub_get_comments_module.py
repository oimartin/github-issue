# import dependencies
from github import Github
from config import access_token
import re
import argparse


parser = argparse.ArgumentParser(description='Get comments from GitHub issues')
parser.add_argument('issue_id', type=int, help='need issue id to continue')
parser.add_argument('GitHub_token', type=str, help='Put in personal token')

args = parser.parse_args()
print(type(args.issue_id))
print(args.issue_id)  

# Connect to learn-github-action repo
connect = Github(args.GitHub_token)
learn_github_action = connect.get_repo("dictybase-playground/learn-github-action") 

# Loop through all issues
for issue in learn_github_action.get_issues(state='open'):
    if args.issue_id == issue.id:

    # See if issue body has an @ to find an email
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