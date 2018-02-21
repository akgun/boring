from unittest.mock import patch

from click.testing import CliRunner

from boring.cli import cli


@patch('boring.cli.pocket')
def test_pocket_add_no_arg(mock_pocket):
    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'add'])

    mock_pocket.pocket_add.assert_called_with([])


@patch('boring.cli.util')
@patch('boring.cli.pocket')
def test_pocket_add_stream(mock_pocket, mock_util):
    mock_util.read_stream.return_value = ['http://url1.com', 'http://url2.com']

    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'add'])

    mock_pocket.pocket_add.assert_called_with(['http://url1.com', 'http://url2.com'])


@patch('boring.cli.pocket')
def test_pocket_add_one_arg(mock_pocket):
    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'add', 'http://url1.com'])

    mock_pocket.pocket_add.assert_called_with(('http://url1.com', ))


@patch('boring.cli.pocket')
def test_pocket_add_one_arg(mock_pocket):
    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'add', 'http://url1.com', 'http://url2.com'])

    mock_pocket.pocket_add.assert_called_with(('http://url1.com', 'http://url2.com'))


@patch('boring.cli.pocket')
def test_pocket_list(mock_pocket):
    mock_pocket.pocket_list.return_value = ['http://article1', 'http://article2']

    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'list'])

    assert 'http://article1' in result.output
    assert 'http://article2' in result.output


@patch('boring.cli.pocket')
def test_pocket_feed(mock_pocket):
    runner = CliRunner()
    result = runner.invoke(cli, ['pocket', 'feed'])

    mock_pocket.pocket_list.assert_called_with(tag='feed')


@patch('boring.cli.wiki')
def test_wiki_list(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=True, news=True, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_tfa(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '--no-tfa'])

    mock_wiki.get_articles.assert_called_with(tfa=False, most_read=True, news=True, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_tfa_short(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '-t'])

    mock_wiki.get_articles.assert_called_with(tfa=False, most_read=True, news=True, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_most_read(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '--no-most-read'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=False, news=True, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_most_read_short(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '-m'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=False, news=True, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_news(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '--no-news'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=True, news=False, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_news_short(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '-n'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=True, news=False, on_this_day=True)


@patch('boring.cli.wiki')
def test_wiki_list_no_on_this_day(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '--no-on-this-day'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=True, news=True, on_this_day=False)


@patch('boring.cli.wiki')
def test_wiki_list_no_on_this_day_short(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '-o'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=True, news=True, on_this_day=False)


@patch('boring.cli.wiki')
def test_wiki_list_mixed(mock_wiki):
    runner = CliRunner()
    result = runner.invoke(cli, ['wiki', 'list', '-mo'])

    mock_wiki.get_articles.assert_called_with(tfa=True, most_read=False, news=True, on_this_day=False)


@patch('boring.cli.feed')
def test_feed_parse_no_url(mock_feed):
    runner = CliRunner()
    result = runner.invoke(cli, ['feed', 'parse'])

    mock_feed.parse_all.assert_called_with([])


@patch('boring.cli.feed')
def test_feed_parse_one_url(mock_feed):
    runner = CliRunner()
    result = runner.invoke(cli, ['feed', 'parse', 'http://feed1'])

    mock_feed.parse_all.assert_called_with(('http://feed1', ))


@patch('boring.cli.feed')
def test_feed_parse_two_url(mock_feed):
    runner = CliRunner()
    result = runner.invoke(cli, ['feed', 'parse', 'http://feed1', 'http://feed2'])

    mock_feed.parse_all.assert_called_with(('http://feed1', 'http://feed2'))


@patch('boring.cli.util')
@patch('boring.cli.feed')
def test_feed_parse_stream(mock_feed, mock_util):
    mock_util.read_stream.return_value = ['http://feed1', 'http://feed2']

    runner = CliRunner()
    result = runner.invoke(cli, ['feed', 'parse'])

    mock_feed.parse_all.assert_called_with(['http://feed1', 'http://feed2'])
