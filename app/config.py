import os


class Config:
    pocketConsumerKey = os.environ.get('BORING_POCKET_CONSUMER_KEY')
    pocketAccessToken = os.environ.get('BORING_POCKET_ACCESS_TOKEN')
