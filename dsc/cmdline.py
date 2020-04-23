"""Handle commandline arguements."""
import argparse
from collections import namedtuple


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
        '--apicall', required=True,
        help='connected to webiste for mailgun API')
    parser.add_argument(
        '--apikey', required=False,
        help='mailgun API key')
    parser.add_argument(
        '--token', required=True, help='github personal token')
    parser.add_argument(
        '--domain', help='domain associated with from email')
    args = parser.parse_args()
    return args


def cmdline_tuple(args):
    params = namedtuple('params',
                        ['organization', 'repository', 'issueid',
                         'label', 'apicall', 'apikey', 'token', 'domain'])
    issue_order = params(organization=args.organization,
                         repository=args.repository,
                         issueid=args.issueid,
                         label=args.label,
                         apicall=args.apicall,
                         apikey=args.apikey,
                         token=args.token,
                         domain=args.domain)
    return issue_order
