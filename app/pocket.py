from pocket import Pocket

from .config import Config


pocket = Pocket(Config.pocketConsumerKey, Config.pocketAccessToken)


def pocket_add(url, tag='boring'):
    if not url: return
    pocket.add(url, tags=tag)


def pocket_bulk_add(urls, tag='boring'):
    for url in urls:
        pocket.bulk_add(url=url, tags=tag)
    if urls:
        pocket.commit()


def pocket_list(tag='boring'):
    response = pocket.get(state='all', tag=tag)
    data_list = response[0]['list']
    if not data_list:
        return []
    links = [article['given_url'] for article in data_list.values()]
    return links
