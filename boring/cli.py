import click

from . import util
from . import pocket
from . import feed
from . import wiki
from . import quote
from . import eksiseyler


@click.group()
def cli():
    """Boooring"""


@cli.group('pocket')
def grppocket():
    """Interacts with pocket"""


@cli.group('wiki')
def grpwiki():
    """Interacts with wiki api"""


@cli.group('feed')
def grpfeed():
    """Interacts with feeds"""


@cli.group('quote')
def grpquote():
    """Interacts with wikiquote"""


@cli.group('eksi')
def grpeksi():
    """Interacts with eksiseyler"""


@grppocket.command('add')
@click.argument('url', nargs=-1)
def cmd_pocket_add(url):
    """Add new article to pocket"""
    if not url:
        url = util.read_stream()
    pocket.pocket_add(url)


@grppocket.command('list')
@click.option('--state', '-s', default='all',
    type=click.Choice(['unread', 'archive', 'all']),
    help='Article read state')
def cmd_pocket_list(state):
    """List articles in pocket"""
    for link in pocket.pocket_list(state=state):
        click.echo(link)


@grppocket.command('feed')
def cmd_pocket_feed():
    """List feed urls in pocket"""
    for link in pocket.pocket_list(tag='feed'):
        click.echo(link)


@grpwiki.command('list')
@click.option('--no-tfa', '-t', default=False, is_flag=True, help='Disable today\'s featured article')
@click.option('--no-most-read', '-m', default=False, is_flag=True, help='Disable most read articles')
@click.option('--no-news', '-n', default=False, is_flag=True, help='Disable new articles')
@click.option('--no-on-this-day', '-o', default=False, is_flag=True, help='Disable on this day articles')
def cmd_wiki_list(no_tfa, no_most_read, no_news, no_on_this_day):
    """Fetch articles from wiki"""
    for article in wiki.get_articles(tfa=not no_tfa,
                                         most_read=not no_most_read,
                                         news=not no_news,
                                         on_this_day=not no_on_this_day):
        click.echo(article)


@grpfeed.command('parse')
@click.argument('url', nargs=-1)
def cmd_feed_parse(url):
    """Get articles from feed url"""
    if not url:
        url = util.read_stream()
    for link in feed.parse_all(url):
        click.echo(link)


@grpquote.command('today')
def cmd_quote_today():
    """Get the quote of the day"""
    click.echo(quote.today())


@grpeksi.command('list')
def cmd_eksi_list():
    for link in eksiseyler.get_links():
        click.echo(link)
