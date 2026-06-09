import pytest
from utils.api_client import ApiClient

VALID_SEARCH_TERM = "Radiohead"
SPECIAL_CHAR_SEARCH_TERM = "AC/DC Rós"
VALID_ARTIST_ID = 657515
VALID_TRACK_ID = 1097861834
VALID_ALBUM_ID = 1097861387

EXPECTED_FIELDS = ["trackName", "artistName", "kind", "collectionName"]

EXPECTED_LOOKUP_FIELDS = ["wrapperType", "kind", "artistId", "artistName", "trackId", "trackName"]

INVALID_ID = 999999999999
INVALID_LONG_ID = 99999999999999999999

# Media type search terms
VALID_PODCAST_SEARCH_TERM = "Serial"
VALID_AUDIOBOOK_SEARCH_TERM = "Harry Potter"

# Media type lookup IDs
VALID_MOVIE_ID = 1745007827  # Titanic: The Musical -- confirmed feature-movie

# Edge case search terms
NUMERIC_SEARCH_TERM = "1984"
LONG_SEARCH_TERM = "a" * 200


@pytest.fixture
def client():
    return ApiClient()