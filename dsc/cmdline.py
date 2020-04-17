"""Handle commandline arguements."""
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
        '--issue-id', type=int, required=True)
    parser.add_argument(
        '--label', required=False)
    parser.add_argument(
        '--token', required=True, help='github personal token')
    return parser.parse_args()
