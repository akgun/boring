from setuptools import setup


setup(
    name='boring',
    version='0.1',
    packages=['boring'],
    install_requires=[
        'click',
        'requests',
        'pocket',
        'feedparser',
        'wikiquote'
    ],
    entry_points={
        'console_scripts': [
            'boring = boring.cli:cli'
        ],
    },
)
