import requests
from lxml import html


URL = 'https://seyler.eksisozluk.com/'


def get_links():
    links = set()
    try:
        page = requests.get(URL)
    except:
        return links
    tree = html.fromstring(page.content)
    for (element, attribute, link, pos) in tree.iterlinks():
        if 'a' == element.tag and 'seyler.eksisozluk.com' in link:
            links.add(link)
    return links
