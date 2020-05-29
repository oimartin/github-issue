import requests
import requests.exceptions


def send(apikey):
    """Send email with mailgun API."""
    try:
        return requests.post(
            'https://api.mailgun.net/v3/sandbox99330cd0068d4a00991aaf3304686e62.mailgun.org/messages',
            auth=('api', apikey),
            data={'from': 'Stock center robot<stockbot@mail.dictycr.org>',
                    'to': 'oimartin1015@gmail.com',
                    'subject': 'DSC Order 4628 - bug',
                    'text': "Test, this is the text part.",
                    'html': """<html>

<body>
<h1>
    Dicty Stock Center
</h1>
<p>
    This is the update.
</p>
</body>

</html>"""
                    })
    except ConnectionError as error:
        raise error
    except requests.exceptions.HTTPError as error:
        raise error
    except requests.exceptions.Timeout as error:
        raise error
