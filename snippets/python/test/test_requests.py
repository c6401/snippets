from unittest.mock import Mock, patch

from requests import Session


@patch.object(Session, "post")
def test_add_supporting_vendor(mock_put: Mock):
    ...
    mock_put.assert_called_with(
        "http://localhost",
        json={},
    )
