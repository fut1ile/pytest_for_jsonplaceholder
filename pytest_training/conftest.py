import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def api_client():
    def request(method, path, **kwargs):
        kwargs.setdefault("timeout", 5)
        return requests.request(method, f"{BASE_URL}{path}", **kwargs)
    return request