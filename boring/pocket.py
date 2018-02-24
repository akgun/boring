from pocket import Pocket

from . import config


pocket = Pocket(config.POCKET_CONSUMER_KEY, config.POCKET_ACCESS_TOKEN)


def pocket_add(urls, tag='boring'):
    if not urls: return
    new_urls = set(urls) - set(pocket_list())
    if not new_urls: return
    for url in new_urls:
        print('Adding "%s".' % url)
        pocket.bulk_add(None, url=url, tags=tag)
    pocket.commit()


def pocket_list(tag='boring', state='all'):
    response = pocket.get(tag=tag, state=state)
    data_list = response[0]['list']
    if not data_list:
        return []
    links = [article['given_url'] for article in data_list.values()]
    return links
