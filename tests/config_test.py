from app.config import _read_feed_file
from . import getdatafile


def test_read_feeds1():
    links = _read_feed_file(getdatafile('data/feeds1.txt'))

    assert [
        'http://feed1',
        'http://feed2'
    ] == links


def test_read_feeds2():
    links = _read_feed_file(getdatafile('data/feeds2.txt'))

    assert [
        'http://feed1',
        'http://feed2'
    ] == links