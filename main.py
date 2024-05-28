from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from feeds.AWSFeed import AWSFeed
from feeds.AzureFeed import AzureFeed
from feeds.GCPFeed import GCPFeed
from report import create_report

app = FastAPI()


@app.get("/aws", response_class=HTMLResponse)
def aws_report():
    filtered_entries = []
    aws_feed = AWSFeed(filtered_entries)
    aws_feed.fetch_parsed_feed()
    return create_report(filtered_entries, aws_feed)


@app.get("/gcp", response_class=HTMLResponse)
def gcp_report():
    filtered_entries = []
    gcp_feed = GCPFeed(filtered_entries)
    gcp_feed.fetch_parsed_feed()
    return create_report(filtered_entries, gcp_feed)


@app.get("/azure", response_class=HTMLResponse)
def azure_report():
    filtered_entries = []
    azure_feed = AzureFeed(filtered_entries)
    azure_feed.fetch_parsed_feed()
    return create_report(filtered_entries, azure_feed)
