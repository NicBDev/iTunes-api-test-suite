import pytest
from utils.api_client import ApiClient

VALID_SEARCH_TERM = "Radiohead"
VALID_ARTIST_ID = 657515
VALID_TRACK_ID = 1097861834
VALID_ALBUM_ID = 1097861387

EXPECTED_FIELDS = ["trackName", "artistName", "kind", "collectionName"]

@pytest.fixture
def client():
    return ApiClient()