# ProxyCrawl

An easy-to-use Python library for scraping and crawling websites using [ProxyCrawl](https://proxycrawl.com) API.

![Python Version](https://img.shields.io/pypi/pyversions/Django.svg)
![License](https://img.shields.io/github/license/mashape/apistatus.svg)

## What is ProxyCrawl?

ProxyCrawl allows you scrape while being anonymous and bypass any restriction, blocks or captchas. 

For more information and registration, please go to [proxycrawl.com](https://proxycrawl.com/).

## Registration

To use ProxyCrawl API, you need to register an account and get your token at [proxycrawl.com](https://proxycrawl.com/)

## Installation

Installing from GitHub (bash):

```bash
pip3 install git+https://github.com/SYAN83/proxycrawl
```

Installing from PyPi is not available yet.

## How to use

`proxycrawl` supports `GET`, `PUT`, and `POST` methods.
 
`proxycrawl` uses `requests.Session` objects in the backend to make API calls and returns `requests.Response` objects. You can pass the same parameters to those methods as you usually do with `requests`.

Here's a simple use case:

```python
from proxycrawl import ProxyCrawlAPI

# You can find your token under Dashboard / API Documentation / URL parameters at proxycrawl.com after registration
api = ProxyCrawlAPI(token='****************')
response = api.get(url='<The website URL you want to scrape>')
print(response.text)

```

To verify that the IP address changes every time when you make a request call, you can run:

```python
response = api.test()
print(response.json())
```
