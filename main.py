import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from feeds.AWSFeed import AWSFeed
from feeds.AzureFeed import AzureFeed
from feeds.GCPFeed import GCPFeed
from report import create_report

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI()


def generate_report(feed_class, feed_name):
    """
    Generate a report using the provided feed class.
    """
    logging.info(f"Starting {feed_name} report generation")
    filtered_entries = []
    feed = feed_class(filtered_entries)
    try:
        feed.fetch_parsed_feed()
    except Exception as e:
        logging.error(f"Failed to fetch and parse {feed_name} feed: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate report")
    logging.info(f"Finished fetching and parsing {feed_name} feed")
    report = create_report(filtered_entries, feed)
    logging.info(f"Finished {feed_name} report generation")
    return report


@app.get("/aws", response_class=HTMLResponse)
def aws_report():
    return generate_report(AWSFeed, "AWS")


@app.get("/gcp", response_class=HTMLResponse)
def gcp_report():
    return generate_report(GCPFeed, "GCP")


@app.get("/azure", response_class=HTMLResponse)
def azure_report():
    return generate_report(AzureFeed, "Azure")
