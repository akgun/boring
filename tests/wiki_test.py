from boring.wiki import get_tfa, get_most_read, get_news, get_on_this_day
from . import read_json_data_file


def test_get_tfa():
    data = read_json_data_file('data/wiki.json')

    tfa = get_tfa(data)

    assert [
        'https://en.wikipedia.org/wiki/Tropical_Depression_Ten_(2005)'
    ] == tfa


def test_get_most_read():
    data = read_json_data_file('data/wiki.json')

    most_read = get_most_read(data)

    assert 'https://en.wikipedia.org/wiki/2018_Winter_Olympics' in most_read
    assert 'https://en.wikipedia.org/wiki/Hope_Hicks' in most_read


def test_get_news():
    data = read_json_data_file('data/wiki.json')

    news = get_news(data)

    assert 'https://en.wikipedia.org/wiki/Maya_Biosphere_Reserve' in news


def test_get_on_this_day():
    data = read_json_data_file('data/wiki.json')

    on_this_day = get_on_this_day(data)

    assert 'https://en.wikipedia.org/wiki/Low_Earth_orbit' in on_this_day
