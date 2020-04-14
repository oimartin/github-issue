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
        '--issue_id', type=int, required=True)
    parser.add_argument(
        '--label', required=False)
    parser.add_argument(
        '--token', required=True, help='github personal token')
    return parser.parse_args()


def github_repo(args):
    """Connect to Github repo.

    Returns:
        --org/repo -- info for API connect

    """
    connect = Github(args.token)
    return connect.get_repo(f"{args.organization}/{args.repository}")


def issue_comments(repo, id, label):
    """Output issue content.

    Arguments:
        repo -- github repository api object
        id -- issue id

    """
    issue = repo.get_issue(number=id)
    trigger_label = repo.get_label(label)

    if '@' in issue.body:
        emails = re.findall('\\S+@\\S+', issue.body)
        shipping_email = emails[0]
        billing_email = emails[1]

    order_line = re.split("\n+", issue.body)[1]
    order_id = re.findall(r'\d+', order_line)[0]

    return shipping_email, billing_email, order_id, trigger_label


def main():
    """Execute other functions in script.

    Executes:
        parse_cmdline() -- command-line interface
        github_repo -- connect to org/repo
        issue_comments -- output issue content
    """
    args = parse_cmdline()
    repo = github_repo(args)
    issue_comments(repo, args.issue_id, args.label)


if __name__ == "__main__":
    main()
