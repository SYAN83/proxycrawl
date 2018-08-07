import scrapy
from urllib.parse import quote_plus


def scrapyProxyRequest(token: str):
    class ScrapyProxyRequest(scrapy.http.Request):
        """
        Scrapy ProxyCrawl API
        """
        API_URL = 'https://api.proxycrawl.com/?token={}&url='.format(token)

        def __init__(self, url, *args, **kwargs):
            url = self.API_URL + quote_plus(url)
            super().__init__(url, *args, **kwargs)
    return ScrapyProxyRequest
