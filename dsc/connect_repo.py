"""Connect to GitHub Repository."""
from github import Github


def github_repo(token, organization, repository):
    """Connect to Github repo.

    Returns:
        --org/repo -- info for API connect

    """
    connect = Github(token)
    return connect.get_repo(f'{organization}/{repository}')