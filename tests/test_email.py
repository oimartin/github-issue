from nose.tools import assert_is_not_none
from unittest.mock import Mock, patch
from info_email import Email
from dsc.params import SendEmailParams


@patch('dsc.email.requests.post')
def test_send(mock_get):

    mock_get.return_value.ok = True
    response = Email.send()
    assert_is_not_none(response)
