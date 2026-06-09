from conftest import VALID_SEARCH_TERM, VALID_ARTIST_ID, EXPECTED_FIELDS, SPECIAL_CHAR_SEARCH_TERM

def test_valid_search_returns_200(client):
    response = client.search(VALID_SEARCH_TERM)
    assert response.status_code == 200


def test_results_contain_expected_fields(client):
    response = client.search(VALID_SEARCH_TERM)
    data = response.json()
    assert all(field in result for result in data["results"] for field in EXPECTED_FIELDS), f"Not all expected fields {EXPECTED_FIELDS} found in API response."

def test_limit_param_caps_results(client):
    result_limit = 5
    response = client.search(search_term=VALID_SEARCH_TERM,limit=result_limit)
    data = response.json()
    assert len(data["results"]) <= result_limit

def test_media_param_filters_correctly(client):
    response = client.search(search_term=VALID_SEARCH_TERM,media_type="music")
    data = response.json()
    assert all(result["kind"] == "song" for result in data["results"])


def test_special_characters_handled(client):
    response = client.search(search_term=SPECIAL_CHAR_SEARCH_TERM)
    assert response.status_code == 200

def test_empty_search_term(client):
    response = client.search("")
    data = response.json()
    assert data["resultCount"] == 0
    assert data["results"] == []
    