from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch()

INDEX = "stackoverflow"
DOC_TYPE = "questions"

mapping = {
    DOC_TYPE: {
        "properties": {
            "title": {
                "type": "text",
                "index": "true"
            },
            "body": {
                "type": "keyword",
                "index": "false"
            }
        }
    }
}

# create index
es.indices.create(index=INDEX, ignore=400)
es.indices.put_mapping(index=INDEX, doc_type=DOC_TYPE, body=mapping)
