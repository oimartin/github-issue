from nose.tools import assert_is_not_none
from unittest.mock import Mock, patch
from tests.info_email import send
from tests.config import apikey


@patch('dsc.email.requests.post')
def test_send(mock_get):

    mock_get.return_value.ok = True
    response = send(apikey)
    assert_is_not_none(response)
