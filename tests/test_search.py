from conftest import VALID_SEARCH_TERM, VALID_ARTIST_ID, EXPECTED_FIELDS

def test_valid_search_returns_200(client):
    result = client.search(VALID_SEARCH_TERM)
    assert result.status_code == 200


def test_results_contain_expected_fields(client):
    # Arrange + Act
    response = client.search(VALID_SEARCH_TERM)
    data = response.json()
    # Assert
    assert all(field in result for result in data["results"] for field in EXPECTED_FIELDS), "Not all expected fields [{EXPECTED_FIELDS}] found in API response."



# def test_media_param_filters_correctly(client):
#     result = 
#     assert

# def test_special_characters_handled(client):

# def test_empty_search_term(client):
#     result = client.search("")
#     assert result
    