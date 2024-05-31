import concurrent.futures
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

    def process_entries(self, entries, one_week_ago):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_entry, entry, one_week_ago) for entry in entries]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.filtered_entries.append(result)

        return self.filtered_entries

    def get_entry_key(self):
        """
        Get entry key
        :return: summary as the default key
        """
        return 'summary'
