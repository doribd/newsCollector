from report import create_report
from rss import fetch_parsed_feed


def main():
    """
    Collecting news from aws, summarize it using OpenAI and creates a html table.

    :return: creates a html table file.
    """
    filtered_entries = []

    fetch_parsed_feed(filtered_entries)

    create_report(filtered_entries)


if __name__ == '__main__':
    main()
