import click

from app.pocket import pocket_add, pocket_list
import app.feed
import app.wiki


@click.group()
def cli():
    """Boooring"""
    pass


@cli.group()
def pocket():
    """Interacts with pocket"""
    pass


@cli.group()
def wiki():
    """Interacts with wiki api"""
    pass


@cli.group()
def feed():
    """Interacts with feeds"""
    pass


# Pocket commands

@pocket.command('add')
@click.argument('url', nargs=-1)
def cmd_pocket_add(url):
    """Add new article to pocket"""
    if not url:
        # Try pipe
        stdin = click.get_text_stream('stdin')
        if not stdin.isatty():
            url = [line.strip() for line in stdin]
    pocket_add(url)


@pocket.command('list')
def cmd_pocket_list():
    """List articles in pocket"""
    for link in pocket_list():
        click.echo(link)


@pocket.command('feed')
def cmd_pocket_feed():
    """List feed urls in pocket"""
    for link in pocket_list(tag='feed'):
        click.echo(link)


# Wiki commands

@wiki.command('list')
@click.option('--no-tfa', '-t', default=False, is_flag=True, help='Disable today\'s featured article')
@click.option('--no-most-read', '-m', default=False, is_flag=True, help='Disable most read articles')
@click.option('--no-news', '-n', default=False, is_flag=True, help='Disable new articles')
@click.option('--no-on-this-day', '-o', default=False, is_flag=True, help='Disable on this day articles')
def cmd_wiki_list(no_tfa, no_most_read, no_news, no_on_this_day):
    """Fetch articles from wiki"""
    for article in app.wiki.get_articles(tfa=not no_tfa,
                                         most_read=not no_most_read,
                                         news=not no_news,
                                         on_this_day=not no_on_this_day):
        click.echo(article)


# Feed commands

@feed.command('parse')
@click.argument('url', nargs=-1)
def cmd_feed_parse(url):
    """Get articles from feed url"""
    if not url:
        # Try pipe
        stdin = click.get_text_stream('stdin')
        if not stdin.isatty():
            url = [line.strip() for line in stdin]
    for link in app.feed.parse_all(url):
        click.echo(link)


if __name__ == '__main__':
    cli()
