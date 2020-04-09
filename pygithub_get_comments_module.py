"""Use PyGithub to connect to Github API v3.

Returns:
    class -- github connects with Github API v3

"""
from github import Github
import re
import argparse


def parse_cmdline():
    """Command-line interface.

    Returns:
        --parsed info -- info for API connect

    """
    parser = argparse.ArgumentParser(
        description='comments from gitHub issues')
    parser.add_argument(
        "--organization", default='dictyBase',
        help='github organization name')
    parser.add_argument(
        '--repository', default='Stock-Center-Orders',
        help='github repository name')
    parser.add_argument(
        '--issue-id', type=int, required=True,
        help='need issue id to continue')
    parser.add_argument(
        '--token', required=True, help='github personal token')
    return parser.parse_args()


def github_repo(args):
    """Connect to Github repo.

    Returns:
        --org/repo -- info for API connect

    """
    try:
        connect = Github(args.token)
        return connect.get_repo(f"{args.organization}/{args.repository}")
    except ValueError:
        print(f"Could not connect to repository.")
        print(f"Check spelling of org and repo.")


def issue_comments(repo, id):
    """Output issue content.

    Arguments:
        repo {object} -- github repository api object
        id {string} -- issue id

    """
    issue = repo.get_issue(number=id)
    print(f"This is the first comment of {issue.id}: {issue.body}")
    if '@' in issue.body:
        emails = re.findall('\\S+@\\S+', issue.body)
        print(f"This is an email/s, {emails}, for issue id: {issue.id}")
    else:
        print(f"There are no emails in the first comment of {issue.id}")
    for comment in issue.get_comments():
        print(f"comments of {issue.id}: {comment.id} - {comment.body}")


def main():
    """Execute other functions in script.

    Executes:
        parse_cmdline() -- command-line interface
        github_repo -- connect to org/repo
        issue_comments -- output issue content
    """
    args = parse_cmdline()
    repo = github_repo(args)
    issue_comments(repo, args.issue_id)


if __name__ == "__main__":
    main()
