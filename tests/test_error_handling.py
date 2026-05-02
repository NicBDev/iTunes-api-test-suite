import pytest
import time
from conftest import INVALID_LONG_ID, VALID_SEARCH_TERM

def test_overly_long_id_raises_exception(client):
    with pytest.raises(Exception):
        client.lookup(INVALID_LONG_ID)

def test_response_time_within_threashold(client):
    start = time.time()
    client.search(search_term=VALID_SEARCH_TERM,media_type="music")
    elapsed = time.time() - start
    assert elapsed < 5

