import feedparser

from . import pocket


def parse(url):
    feed =  feedparser.parse(url)
    return [entry.link for entry in feed['entries']]


def parse_all(urls):
    links = []
    for url in urls:
        links.extend(parse(url))
    return links


def get():
    feed_links = pocket.pocket_list(tag='feed')
    return parse_all(feed_links)
