from collections import namedtuple

GithubParams = namedtuple('GithubParams',
                          ['token',
                           'repository',
                           'organization'
                           ])

OrderParams = namedtuple('OrderParams',
                         ['order_id',
                          'user_name',
                          'shipping_email',
                          'consumer_email'
                          ])

MailgunEmailParams = namedtuple('MailgunEmailParams',
                                ['endpoint',
                                 'api_key'
                                 ])

SendEmailParams = namedtuple('SendEmailParams',
                             ['from',
                              'to',
                              'content',
                              'subject'
                              ])
