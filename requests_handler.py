import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class RequestsHandler:
    def __init__(self, retries=3, backoff_factor=0.3, status_forcelist=(500, 502, 504), session=None):
        self.session = session or requests.Session()
        retry_strategy = Retry(
            total=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

    def get(self, url, params=None, **kwargs):
        return self.session.get(url, params=params, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.session.post(url, data=data, json=json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.session.put(url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.session.delete(url, **kwargs)

handler = RequestsHandler(retries=5)

# Get request
response = handler.get("http://httpbin.org/get")
print(response.json())

# Post request
response = handler.post("http://httpbin.org/post", json={"key": "value"})
print(response.json())