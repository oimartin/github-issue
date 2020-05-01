"""Send order info into a namedtuple."""
from collections import namedtuple


def order_info(body, args):
    """Order info from body and commandline arguements in a namedtuple."""
    organize = namedtuple('organize', ['issue_id', 'user_name',
                                       'shipping_email', 'trigger_label',
                                       'mailgun_key', 'mailgun_apicall',
                                       'mailgun_domain'])
    info = organize(issue_id=body.order_id,
                    user_name=body.user_name,
                    shipping_email=body.shipping_email,
                    trigger_label=args.label,
                    mailgun_key=args.apikey,
                    mailgun_apicall=args.apicall,
                    mailgun_domain=args.domain)
    return info
