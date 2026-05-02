
from conftest import VALID_ARTIST_ID, VALID_TRACK_ID, INVALID_ID, EXPECTED_LOOKUP_FIELDS


def test_valid_lookup_returns_correct_entity(client):
    response = client.lookup(VALID_ARTIST_ID)
    data = response.json()
    assert data["results"][0]["artistId"] == VALID_ARTIST_ID
    assert data["results"][0]["wrapperType"] == "artist"

    
def test_response_schema_matches_expected(client):
    response = client.lookup(VALID_TRACK_ID)
    data = response.json()
    assert all(field in result for result in data["results"] for field in EXPECTED_LOOKUP_FIELDS), f"Not all expected fields {EXPECTED_LOOKUP_FIELDS} found in API lookup response."

def test_invalid_id_returns_expected_response(client):
    response = client.lookup(INVALID_ID)
    data = response.json()
    assert data["resultCount"] == 0
    assert data["results"] == []

