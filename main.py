import click

from app.pocket import pocket_add, pocket_bulk_add, pocket_list
import app.feed
import app.wiki


@click.group()
def cli():
    pass


@cli.command('add', help='Add new article to pocket')
@click.argument('url')
def add(url):
    pocket_add(url)


@cli.command('list', help='List articles in pocket')
def list_all():
    for link in pocket_list():
        click.echo(link)


@cli.command('find', help='Find articles and save to pocket')
@click.option('--no-wiki', is_flag=True, default=False, help='Disable wiki find')
@click.option('--no-feed', is_flag=True, default=False, help='Disable rss feed find')
def find(no_wiki, no_feed):
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


@cli.command('feed', help='Parse feed url to test')
@click.argument('url')
def feed(url):
    click.echo('Found links:')
    for link in app.feed.parse(url):
        click.echo(link)


if __name__ == '__main__':
    cli()
