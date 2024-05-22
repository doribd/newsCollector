from feeds.AWSFeed import AWSFeed
from report import create_report


def main():
    """
    Collecting news from aws, summarize it using OpenAI and creates a html table.

    :return: creates a html table file.
    """
    filtered_entries = []

    aws_feed = AWSFeed(filtered_entries)
    aws_feed.fetch_parsed_feed()

    create_report(filtered_entries)


if __name__ == '__main__':
    main()
