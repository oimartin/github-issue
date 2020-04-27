"""Send order info into a dictionary."""


def dict_order_info(body, args):
    """Order info from issue body and commandline arguements in a dict."""
    info = {'id': body.order_id,
            'user_name': body.user_name,
            'shipping_email': body.shipping_email,
            'trigger_label': args.label,
            'mailgun_key': args.apikey,
            'mailgun_apicall': args.apicall,
            'mailgun_domain': args.domain}
    return info
