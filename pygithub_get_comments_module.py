# import dependencies
from github import Github
import re
import argparse

# Use argeparse to set up issue_id to search and GitHub access token to connect with
def get_issue_id_and_token():
    parser = argparse.ArgumentParser(description='Get comments from GitHub issues')
    parser.add_argument('issue_id', type=int, help='need issue id to continue')
    parser.add_argument('GitHub_token', type=str, help='Put in personal token')

    args = parser.parse_args()
    issue_id = args.issue_id
    access_token = args.GitHub_token

    print(f"main() worked")
    return issue_id, access_token

# Connect to learn-github-action repo
def connect_token_pyGithub(access_token):
    connect = Github(access_token)
    learn_github_action = connect.get_repo("dictybase-playground/learn-github-action") 
    print(f"connect_token_pyGithub() worked")
    return learn_github_action
    

def getting_issue_comments(learn_github_action, issue_id):
    # Loop through all issues
    for issue in learn_github_action.get_issues(state='open'):
        print(f"This is the issue.id or from the for loop used {issue.id}")
        if issue_id == issue.id:

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

def main():
    issue_id, access_token = get_issue_id_and_token()
    learn_github_action = connect_token_pyGithub(access_token)
    getting_issue_comments(learn_github_action, issue_id)

if __name__ == "__main__":
    main()