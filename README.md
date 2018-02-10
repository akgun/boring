# Boring

## What is this?

A command line application that saves articles to [Pocket](https://getpocket.com). Saved articles will have tag **boring**.

### Wikipedia

It fetches featured articles from [Wikipedia](https://www.wikipedia.org/).

### RSS feeds

When you save a RSS link (for ex; [NASA RSS](https://www.nasa.gov/rss/dyn/breaking_news.rss)) with tag **feed**, application will fetch articles from RSS and save them.

## Installation

Change directory.

`$ cd boring`

Create virtualenv.

`$ python3 -m venv venv`

Activate virtual env.

`$ . venv/bin/activate`

Install requirements.

`$ pip install -r requirements.txt`

Build executable.

`$ pyinstaller --onefile main.spec`

Run executable with your credentials.

`$ BORING_POCKET_CONSUMER_KEY=<your consumer key> BORING_POCKET_ACCESS_TOKEN=<your access token> ./dist/boring`

For obtaining tokens, read this [article](http://www.jamesfmackenzie.com/getting-started-with-the-pocket-developer-api/).