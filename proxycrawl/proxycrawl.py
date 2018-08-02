import requests


class ProxyCrawlAPI(object):
    """

    """

    API_URL = 'https://api.proxycrawl.com/'
    TEST_URL = 'https://httpbin.org/ip'

    def __init__(self, token: str):
        self.token = token
        self.session = requests.Session()

    def post(self, url: str, data=None, json=None, **kwargs):
        return self._request(method='post', url=url, data=data, json=json, **kwargs)

    def get(self, url: str, **kwargs):
        return self._request(method='get', url=url, **kwargs)

    def put(self, url, data=None, **kwargs):
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