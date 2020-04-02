# import dependencies
from github import Github
import re
import argparse


def get_issue_id_and_token():
    parser = argparse.ArgumentParser(
        description='comments from gitHub issues')
    parser.add_argument(
        "--organization", default='dictyBase', help='github organization name') 
    parser.add_argument(
        '--repository', default='Stock-Center-Orders',
        help='github repository name')
    parser.add_argument(
        '--issue-id', type=int, required=True,
        help='need issue id to continue')
    parser.add_argument(
        '--token', required=True, help='github personal token')
    args = parser.parse_args()
    return args


# Connect to learn-github-action repo
def connect_token_pyGithub(access_token):
    connect = Github(access_token)
    learn_github_action = connect.get_repo("dictybase-playground/learn-github-action") 
    return learn_github_action
    

def getting_issue_comments(learn_github_action, issue_id):
    # Loop through all issues
    for issue in learn_github_action.get_issues(state='open'):
        
        # If issue id entered matches on of the open issue ids
        if issue_id == issue.id:
            
            # Print just the issue id and body of first comment
            print(f"This is the first comment of {issue.id}: {issue.body}")

        # See if issue body has an @ to find an email
            if '@' in issue.body:
                
                # Find emails and store in list
                emails = re.findall('\S+@\S+', issue.body)
                print(f"This is an email/s, {emails}, for issue id: {issue.id}")
            else:
                print(f"There are no emails in the first comment of {issue.id}")
            
        # Loop through all comments of specific issue
            for comment in issue.get_comments():

                # Print issue id, comment id, and the following comments
                print(f"These are the following comments of {issue.id}: {comment.id} - {comment.body}")
            else:
                print(f"There are no additional comments for {issue.id}")

def main():
    issue_id, access_token = get_issue_id_and_token()
    learn_github_action = connect_token_pyGithub(access_token)
    getting_issue_comments(learn_github_action, issue_id)

if __name__ == "__main__":
    main()