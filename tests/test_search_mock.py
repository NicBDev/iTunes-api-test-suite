import pytest
import requests
from conftest import VALID_SEARCH_TERM, EXPECTED_FIELDS

def test_search_returns_200_offline(client, mocker):
    # Step 1 -- Build the fake response object
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "resultCount": 2,
        "results": [
            {
                "trackName": "Fake Track 1",
                "artistName": "Radiohead",
                "kind": "song",
                "collectionName": "Fake Album"
            },
            {
                "trackName": "Fake Track 2", 
                "artistName": "Radiohead",
                "kind": "song",
                "collectionName": "Fake Album"
            }
        ]
    }
    
    # Step 2 -- Intercept requests.get and return our fake response
    mocker.patch("utils.api_client.requests.get", return_value=mock_response)
    
    # Step 3 -- Call the real client as normal
    response = client.search(VALID_SEARCH_TERM)
    
    # Step 4 -- Assert
    assert response.status_code == 200

def test_search_returns_500_offline(client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("500")
    mocker.patch("utils.api_client.requests.get", return_value=mock_response)

    with pytest.raises(Exception):
        client.search(VALID_SEARCH_TERM)


def test_search_connection_error_offline(client, mocker):
    mocker.patch("utils.api_client.requests.get", side_effect=requests.exceptions.ConnectionError())

    with pytest.raises(Exception):
        client.search(VALID_SEARCH_TERM)

def test_search_timeout_offline(client, mocker):
    mocker.patch("utils.api_client.requests.get", side_effect=requests.exceptions.Timeout())

    with pytest.raises(Exception):
        client.search(VALID_SEARCH_TERM)

def test_results_not_contain_expected_fields(client, mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
    "resultCount": 1,
    "results": [
        {
            "artistName": "Radiohead",
            "kind": "song",
            # trackName and collectionName deliberately missing!
        }
    ]
    }
    mocker.patch("utils.api_client.requests.get", return_value=mock_response)
    
    response = client.search(VALID_SEARCH_TERM)
    data = response.json()
    assert not all(field in result for result in data["results"] for field in EXPECTED_FIELDS)

