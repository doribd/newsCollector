from overrides import overrides

from feeds.rss_feed import RSSFeed


class AWSFeed(RSSFeed):
    """
    AWS Feed class.
    """

    def __init__(self, url):
        super().__init__(url)

    @overrides
    def process_entry(self, entry, one_week_ago):
        """
        Process single feed.
        :param entry: to be processed
        :param one_week_ago: published date to be filtered
        """
        pass

    @overrides
    def fetch_parsed_feed(self, filtered_entries):
        """
        Fetching the feed to be parsed.
        :param filtered_entries:  list
        :return:  list
        """
        pass
