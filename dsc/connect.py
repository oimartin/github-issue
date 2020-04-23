"""Connect to GitHub Repository."""
from github import Github


def github_repo(issue):
    """Connect to Github repo.

    Returns:
        --org/repo -- info for API connect

    """
    connect = Github(issue[6])
    return connect.get_repo(f'{issue[0]}/{issue[1]}')
