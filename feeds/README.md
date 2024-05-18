# Feeds Directory

This directory contains the classes for handling RSS feeds from different sources.

## Files

- `rss_feed.py`: This file contains the `RSSFeed` abstract base class, which defines the common interface for all RSS feed classes.
- `aws_feed.py`: This file contains the `AWSFeed` class, which inherits from `RSSFeed` and implements the methods for fetching and processing AWS RSS feeds.
- `azure_feed.py`: This file contains the `AzureFeed` class, which inherits from `RSSFeed` and implements the methods for fetching and processing Azure RSS feeds.

