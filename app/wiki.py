from datetime import datetime

import requests


API_URL = 'https://en.wikipedia.org/api/rest_v1/feed/featured/%s'
URL = 'https://en.wikipedia.org/wiki/%s'


def get_articles():
    data = requests.get(API_URL % datetime.now().strftime('%Y/%m/%d')).json()
    links = []
    links.append(URL % data['tfa']['title'])
    links.extend([URL % article['title'] for article in data['mostread']['articles']])
    return links
