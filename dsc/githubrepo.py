from collections import namedtuple


def github(cmdline):
    """Create named tuple of info to connect to Github."""
    connect = namedtuple('connect', ['organization', 'repository', 'token'])
    connected = connect(organization=cmdline.organization,
                        repository=cmdline.repository,
                        token=cmdline.token)
    return connected
