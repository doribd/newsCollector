from abc import abstractmethod


class RSSFeed:
    """
        Abstract class for RSS feed.
    """


def __init__(self, url):
    self.url = url


@abstractmethod
def fetch_parsed_feed(self, filtered_entries):
    """
    Fetching the feed to be parsed.
    :param filtered_entries: which is the list of entries to be filtered
    :return: the feed
    """
    pass


@abstractmethod
def process_entry(self, entry, one_week_ago):
    """
    Process single feed.
    :param entry: to be processed
    :param one_week_ago: filter date
    :return: dict
    """
    pass
