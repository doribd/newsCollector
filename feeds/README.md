# Feeds Directory

This directory contains the classes for handling RSS feeds from different sources.

## Files

- `RSSFeed.py`: This file contains the `RSSFeed` abstract base class, which defines the common interface for all RSS feed classes.
- `AWSFeed.py`: This file contains the `AWSFeed` class, which inherits from `RSSFeed` and implements the methods for fetching and processing AWS RSS feeds.
- `AzureFeed.py`: This file contains the `AzureFeed` class, which inherits from `RSSFeed` and implements the methods for fetching and processing Azure RSS feeds.
- `GCPFeed.py`: This file contains the `GCPFeed` class, which inherits from `RSSFeed` and implements the methods for fetching and processing Azure GCP feeds.

