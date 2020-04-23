"""Send order info into a dictionary."""


def dict_order_info(order, issue):
    order = {'id': order[0],
             'user_name': order[1],
             'shipping_email': order[2],
             'trigger_label': issue[3],
             'mailgun_key': issue[5],
             'mailgun_apicall': issue[4],
             'mailgun_domain': issue[7]}
    return order
