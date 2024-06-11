import logging
from configparser import ConfigParser
from datetime import datetime, timedelta
from datetime import timezone

import feedparser
import requests
from dotenv import load_dotenv
from overrides import overrides

from feeds.RSSFeed import RSSFeed
from summarizer import summarize_text
from summarizers.OpenAISummarizer import OpenAISummarizer


class GCPFeed(RSSFeed):
    """
    GCP Feed class.
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
        updated_date = datetime.strptime(entry.updated, '%Y-%m-%dT%H:%M:%S%z')
        now = datetime.now(timezone.utc)
        one_week_ago = now - timedelta(days=7)
        if updated_date >= one_week_ago:
            content_type = self.summarizer.summarize_text(entry['content'])
            return {
                'title': entry.title,
                'link': entry.link,
                'updated': updated_date.strftime('%Y-%m-%d'),
                'content': content_type
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

        rss_url = config.get('RSS', 'gcp_url')

        now = datetime.now()
        num_days = config.getint('DAYS', 'num_days')
        one_week_ago = now - timedelta(days=num_days)

        response = requests.get(rss_url, timeout=5)
        response.encoding = 'utf-8'  # Force utf-8 encoding
        feed_data = response.text

        feed = feedparser.parse(feed_data)
        if feed.bozo:
            logging.error("Failed to parse the RSS feed.")
            print("Failed to parse the RSS feed.")
            exit(1)

        return self.process_entries(feed.entries, one_week_ago)

    @staticmethod
    def get_name():
        return 'GCP'

    @overrides
    def get_entry_key(self):
        return 'content'
