import requests
import aiohttp

from typing import Any, Dict

class ProxyCrawlAPI(object):
    """

    """

    API_URL = 'https://api.proxycrawl.com/'
    TEST_URL = 'https://httpbin.org/ip'

    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def get(self, url: str, **kwargs):
        return self._request(method='get', url=url, **kwargs)

    def post(self, url: str, data: Any=None, json: Dict=None, **kwargs):
        return self._request(method='post', url=url, data=data, json=json, **kwargs)

    def put(self, url, data: Any=None, **kwargs):
        return self._request(method='put', url=url, data=data, **kwargs)

    def _request(self, method: str, url: str, **kwargs):
        if 'params' in kwargs:
            kwargs['params'].update({'token':self.token, 'url':url})
        else:
            kwargs['params'] = {'token':self.token, 'url':url}
        response = getattr(self.session, method)(url=self.API_URL, **kwargs)
        response.raise_for_status()
        return response

    def test(self, url: str=None, **kwargs):
        url = url or self.TEST_URL
        response = self.get(url=url, **kwargs)
        return response

    def close(self):
        self.session.close()



class ProxyCrawlAsyncAPI(object):
    """
    Async HTTP request via ProxyCrawl
    """

    API_URL = 'https://api.proxycrawl.com/'
    TEST_URL = 'https://httpbin.org/ip'

    def __init__(self, token: str, **kwargs):
        self.token = token
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False), **kwargs)

    def get(self, url: str, **kwargs) -> '_RequestContextManager':
        """Perform HTTP GET request."""
        return self._request(method='get', url=url, **kwargs)

    def post(self, url: str, data: Any=None, **kwargs):
        """Perform HTTP POST request."""
        return self._request(method='post', url=url, data=data, **kwargs)

    def put(self, url: str, data: Any=None, **kwargs):
        """Perform HTTP PUT request."""
        return self._request(method='put', url=url, data=data, **kwargs)

    def _request(self, method: str, url: str, **kwargs):
        if 'params' in kwargs:
            kwargs['params'].update({'token':self.token, 'url':url})
        else:
            kwargs['params'] = {'token':self.token, 'url':url}
        response = getattr(self.session, method)(url=self.API_URL, **kwargs)
        return response
