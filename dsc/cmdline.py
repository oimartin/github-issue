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
        '--issueid', type=int, required=True)
    parser.add_argument(
        '--label', required=False)
    parser.add_argument(
        '--endpoint', required=True,
        help='mailgun API endpoint')
    parser.add_argument(
        '--apikey', required=True,
        help='mailgun API key')
    parser.add_argument(
        '--token', required=True, help='github personal token')
    parser.add_argument(
        '--domain', help='domain associated with from email')
    return parser.parse_args()
