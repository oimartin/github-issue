"""Send order info into a dictionary."""


def dict_order_info(order_id, user_name, shipping_email, label, key, domain):
    order = {'id': order_id,
             'user_name': user_name,
             'shipping_email': shipping_email,
             'trigger_label': label,
             'mailgun_key': key,
             'mailgun_domain': domain}
    return order
