import requests

class ApiClient:

    def __init__(self, base_url="https://itunes.apple.com/"):
        self.base_url = base_url

    def search(self, search_term, country_code = "US", media_type = "music", limit = 10):
        return self._get_request_with_error_handling(self.base_url + "search", params={
            "term": search_term,
            "media": media_type,
            "limit": limit,
            "country": country_code
            })
    def lookup(self, media_id, country_code = "US"):
        return self._get_request_with_error_handling(self.base_url + "lookup", params={
            "id": media_id,
            "country": country_code
            })
        

    def _get_request_with_error_handling(self,request_body,params):
        try:
            result = requests.get(request_body, params = params)
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