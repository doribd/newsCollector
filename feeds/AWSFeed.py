import logging
from configparser import ConfigParser
from datetime import datetime, timedelta

import feedparser
from dotenv import load_dotenv
from overrides import overrides

from feeds.RSSFeed import RSSFeed
from summarizer import summarize_text
from summarizers.OpenAISummarizer import OpenAISummarizer


class AWSFeed(RSSFeed):
    """
    AWS Feed class.
    """

    def __init__(self, filtered_entries):
        super().__init__(filtered_entries)
        self.summarizer = OpenAISummarizer()


    @overrides
    def process_entry(self, entry, one_week_ago):
        """
          Process single feed.
          :param entry: to be processed
          :param one_week_ago: published date to be filtered
          :return: dict
          """
        published_date = datetime.strptime(entry.published, '%a, %d %b %Y %H:%M:%S %Z')

        if published_date >= one_week_ago:
            summary = self.summarizer.summarize_text(entry.summary)
            return {
                'title': entry.title,
                'link': entry.link,
                'published': published_date.strftime('%Y-%m-%d'),
                'summary': summary
            }
        return None

    @overrides
    def fetch_parsed_feed(self):
        """
        Fetching the feed to be parsed.
        :return: the feed
        """
        config = ConfigParser()
        config.read('config.ini')
        load_dotenv()

        rss_url = config.get('RSS', 'aws_url')

        now = datetime.now()
        num_days = config.getint('DAYS', 'num_days')
        one_week_ago = now - timedelta(days=num_days)

        feed = feedparser.parse(rss_url)

        if feed.bozo:
            logging.error("Failed to parse the RSS feed.")
            print("Failed to parse the RSS feed.")
            exit(1)

        return self.process_entries(feed.entries, one_week_ago)

    @staticmethod
    def get_name():
        return 'AWS'

    @overrides
    def get_entry_key(self):
        return 'summary'
