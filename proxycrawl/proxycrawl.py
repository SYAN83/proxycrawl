import requests


class ProxyCrawlAPI(requests.Session):
    """
    ProxyCrawl API
    """

    API_URL = 'https://api.proxycrawl.com/'
    TEST_URL = 'https://httpbin.org/ip'

    def __init__(self, token: str):
        self.token = token
        super().__init__()

    def request(self, method: str, url: str, **kwargs):
        if 'params' in kwargs:
            kwargs['params'].update({'token':self.token, 'url':url})
        else:
            kwargs['params'] = {'token':self.token, 'url':url}
        return super().request(method=method, url=self.API_URL, **kwargs)

    def test(self):
        response = self.get(url=self.TEST_URL)
        return response.json()
