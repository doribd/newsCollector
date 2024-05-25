import concurrent.futures
from configparser import ConfigParser
from datetime import datetime, timedelta, timezone

import feedparser
from dotenv import load_dotenv
from overrides import overrides
from pytz import timezone

from feeds.RSSFeed import RSSFeed
from summarizer import summarize_text


class AzureFeed(RSSFeed):
    """
    Azure Feed class.
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
        published = entry.published.replace('Z', '+0000')
        published_date = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')

        # Convert both dates to UTC before comparing
        utc = timezone('UTC')
        published_date = published_date.astimezone(utc)
        one_week_ago = one_week_ago.replace(tzinfo=utc)

        if published_date >= one_week_ago:
            summary = summarize_text(entry.summary)
            return {
                'title': entry.title,
                'link': entry.link,
                'published': published_date.strftime('%Y-%m-%d'),
                'summary': summary,
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

        # Adjust the key to fetch the Azure RSS feed URL from your configuration
        rss_url = config.get('RSS', 'azure_url')

        now = datetime.now()
        num_days = config.getint('DAYS', 'num_days')
        one_week_ago = now - timedelta(days=num_days)

        feed = feedparser.parse(rss_url)

        if feed.bozo:
            print("Failed to parse the RSS feed.")
            exit(1)

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.process_entry, entry, one_week_ago) for entry in feed.entries]

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    self.filtered_entries.append(result)

        return self.filtered_entries

    @staticmethod
    def get_name():
        return 'Azure'
