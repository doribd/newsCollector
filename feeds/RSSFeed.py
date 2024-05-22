from abc import ABC, abstractmethod


class RSSFeed(ABC):
    """
        Abstract class for RSS feed.
    """

    def __init__(self, filtered_entries):
        self.filtered_entries = filtered_entries

    @abstractmethod
    def fetch_parsed_feed(self):
        """
        Fetching the feed to be parsed.
        :param self: the class instance
        :return: the feed
        """
        pass

    @abstractmethod
    def process_entry(self, entry, one_week_ago):
        """
        Process single feed.
        :param self: the class instance
        :param entry: to be processed
        :param one_week_ago: filter date
        :return: dict
        """
        pass
