from conftest import VALID_PODCAST_SEARCH_TERM


def test_podcast_search_returns_podcast_results(client):
    response = client.search(search_term=VALID_PODCAST_SEARCH_TERM, media_type="podcast")
    assert response.status_code == 200
    data = response.json()
    assert data["resultCount"] > 0
    assert all(result["kind"] == "podcast" for result in data["results"])