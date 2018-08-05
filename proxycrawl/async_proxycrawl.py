import aiohttp


class AsyncProxySession(aiohttp.ClientSession):
    """
    Async ProxyCrawl API
    """

    API_URL = 'https://api.proxycrawl.com/'
    TEST_URL = 'https://httpbin.org/ip'

    def __init__(self, token: str, *args, **kwargs):
        self.token = token
        super().__init__(*args, **kwargs)

    async def test(self):
        async with self.get(url=self.TEST_URL) as response:
            return await response.text()

    async def _request(self, method, url, *args, **kwargs):
        if 'params' in kwargs:
            kwargs['params'].update({'token': self.token, 'url': url})
        else:
            kwargs['params'] = {'token': self.token, 'url': url}
        return await super()._request(method=method, url=self.API_URL, *args, **kwargs)