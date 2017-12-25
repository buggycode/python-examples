from datetime import datetime
from elasticsearch import Elasticsearch
import feedparser

es = Elasticsearch()

INDEX = "stackoverflow"
DOC_TYPE = "questions"

RSS = "https://stackoverflow.com/feeds/tag?tagnames=python&sort=featured"
feed = feedparser.parse(RSS)
for entry in feed.entries:
    print(entry.title)
    """
    es.index(index=INDEX, doc_type=DOC_TYPE, body={
        "title": entry.title,
        "body": entry.summary,
        "url": entry.link
    })
    """
    ## analyzer
