from datetime import datetime

import requests


API_URL = 'https://en.wikipedia.org/api/rest_v1/feed/featured/%s'
URL = 'https://en.wikipedia.org/wiki/%s'


def get_articles():
    data = requests.get(API_URL % datetime.now().strftime('%Y/%m/%d')).json()
    links = []
    links.extend(get_tfa(data))
    links.extend(get_most_read(data))
    links.extend(get_news(data))
    links.extend(get_on_this_day(data))
    return links


def get_tfa(data):
    return [URL % data['tfa']['title']]


def get_most_read(data):
    return [URL % article['title'] for article in data['mostread']['articles']]


def get_news(data):
    news = (new for new in data['news'])
    links_list = (new['links'] for new in news)
    links = (item for link in links_list for item in link)
    return [
        URL % link['title'] for link in links
    ]


def get_on_this_day(data):
    onthisdays = (i for i in data['onthisday'])
    pages_list = (onthisday['pages'] for onthisday in onthisdays)
    pages = (item for page in pages_list for item in page)
    return [
        URL % page['title'] for page in pages
    ]
