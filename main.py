import click

from app.pocket import pocket_add, pocket_bulk_add, pocket_list
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
@click.argument('url')
def cmd_pocket_add(url):
    """Add new article to pocket"""
    pocket_add(url)


@pocket.command('list')
def cmd_pocket_list():
    """List articles in pocket"""
    for link in pocket_list():
        click.echo(link)


@pocket.command('populate')
@click.option('--no-wiki', is_flag=True, default=False, help='Disable wiki find')
@click.option('--no-feed', is_flag=True, default=False, help='Disable rss feed find')
def cmd_pocket_populate(no_wiki, no_feed):
    """Find articles and save to pocket"""
    found_links = []
    if not no_feed:
        found_links.extend(app.feed.get())
    if not no_wiki:
        found_links.extend(app.wiki.get_articles())

    # Skip if no new link is found
    if not found_links:
        click.echo('No new link found.')
        return

    existing_links = pocket_list()

    new_links = set(found_links) - set(existing_links)
    if not new_links:
        click.echo('No new link found.')
        return
    for link in new_links:
        click.echo('Found new link \'%s\'.' % link)
    pocket_bulk_add(new_links)


# Wiki commands

@wiki.command('list')
def cmd_wiki_list():
    """Fetch articles from wiki"""
    for article in app.wiki.get_articles():
        click.echo(article)


# Feed commands

@feed.command('parse')
@click.argument('url')
def cmd_feed_parse(url):
    """Parse feed url to test"""
    for link in app.feed.parse(url):
        click.echo(link)


if __name__ == '__main__':
    cli()
