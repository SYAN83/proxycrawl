# ProxyCrawl

An easy-to-use Python HTTP requests library for scraping and crawling websites using [ProxyCrawl API](https://proxycrawl.com).

Currently support requests, aiohttp and scrapy!

![Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)

## What is ProxyCrawl API?

ProxyCrawl API allows you scrape while being anonymous and bypass any restriction, blocks or captchas. 

For more information and registration, please go to [proxycrawl.com](https://proxycrawl.com/).

## Registration

To use ProxyCrawl, you need to register an account and obtain your token at [proxycrawl.com](https://proxycrawl.com/). 
You can find your token under *Dashboard* / *API Documentation* / *URL parameters*.

## Installation

Installing from GitHub (bash):

```bash
pip3 install git+https://github.com/SYAN83/proxycrawl
```

Installing from PyPi is not available yet.

## How to use

`proxycrawl` includes three classes:
 `ProxySession` for synchronous HTTP requests, 
 `AsyncProxySession` for asynchronous HTTP Requests,
  as well as `ScrapyProxyRequest` for scrapy.
 
1. `ProxySession` inherits `requests.Session` class:

    ```python
    from proxycrawl import ProxySession
    
    session = ProxySession(token='****************')
    response = session.get(url='https://github.com/')
    print(response.text)
    ```
    
    To verify that the IP address changes every time when you make a request call, you can run:
    
    ```python
    from proxycrawl import ProxySession
    
    session = ProxySession(token='****************')
    ip = session.test()
    print(ip)
    ```

2. `AsyncProxySession` inherits `aiohttp.ClientSession` class:
    
    ```python
    import aiohttp
    import asyncio
    from proxycrawl import AsyncProxySession
    
    async def fetch(session, url):
        async with session.get(url) as response:
            return await response.text()
    
    async def main():
        async with AsyncProxySession(token='****************', 
                                     connector=aiohttp.TCPConnector(ssl=False)) as session:
            content = await fetch(session=session, url='https://github.com/')
            print(content)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    ``` 
    
    `AsyncProxySession.test()` allows you to verify that the IP address changes in async mode:
    
    ```python
    import aiohttp
    import asyncio
    from proxycrawl import AsyncProxySession
 
    async def main():
        async with AsyncProxySession(token='****************', 
                                     connector=aiohttp.TCPConnector(ssl=False)) as session:
            ip = await session.test()
            print(ip)
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    ``` 

3. `ScrapyProxyRequest` inherits `scrapy.http.Request` class:
    
    ```python
    import scrapy
    from proxycrawl import scrapyProxyRequest
    

    ScrapyProxyRequest = scrapyProxyRequest(token='****************')
 
 
    class QuotesSpider(scrapy.Spider):
        name = "quotes"
    
        def start_requests(self):
            urls = [
                'http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/',
            ]
            for url in urls:
                yield ScrapyProxyRequest(url=url, callback=self.parse)
    
        def parse(self, response):
            page = response.url.split("/")[-2]
            filename = 'quotes-%s.html' % page
            with open(filename, 'wb') as f:
                f.write(response.body)
            self.log('Saved file %s' % filename)
    ```
