import requests

class ApiClient:

    def __init__(self, base_url="https://itunes.apple.com/"):
        self.base_url = base_url

    def search(self, search_term,media_type = "music", limit = 10):
        try:
            result = requests.get(self.base_url + "search", params={
            "term": search_term,
            "media": media_type,
            "limit": limit
            })
            result.raise_for_status()
            return result
        except requests.exceptions.ConnectionError as e:
            raise Exception("A connection error occured") from e
        except requests.exceptions.Timeout as e:
            raise Exception("A Timeout error occured") from e
        except requests.exceptions.HTTPError as e:
            raise Exception("A HTTP error occured") from e
        except requests.exceptions.InvalidURL as e:
             raise Exception("Invalid URL") from e
        except requests.RequestException as e:
            raise Exception("An error occured") from e

    
