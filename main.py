from datetime import datetime

from feeds.AWSFeed import AWSFeed
from feeds.AzureFeed import AzureFeed
from feeds.GCPFeed import GCPFeed
from report import create_report


def main():
    """
    Collecting news from aws, summarize it using OpenAI and creates a html table.

    :return: creates a html table file.
    """

    filtered_entries = []
    gcp_feed = GCPFeed(filtered_entries)
    gcp_feed.fetch_parsed_feed()
    create_report(filtered_entries, gcp_feed)

    filtered_entries = []
    aws_feed = AWSFeed(filtered_entries)
    aws_feed.fetch_parsed_feed()
    create_report(filtered_entries, aws_feed)

    filtered_entries = []
    azure_feed = AzureFeed(filtered_entries)
    azure_feed.fetch_parsed_feed()
    create_report(filtered_entries, azure_feed)


if __name__ == '__main__':
    main()
