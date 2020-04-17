"""Connect to GitHub Repository."""
import cmdline_arg
from github import Github


def github_repo():
    """Connect to Github repo.

    Returns:
        --org/repo -- info for API connect

    """
    token = cmdline_arg.parse_cmdline().args.token
    connect = Github(token)
    organization = cmdline_arg.parse_cmdline().args.organization
    repository = cmdline_arg.parse_cmdline().args.repository
    return connect.get_repo(organization/repository)
