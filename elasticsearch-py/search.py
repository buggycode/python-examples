from datetime import datetime
from elasticsearch import Elasticsearch
import feedparser

es = Elasticsearch()

INDEX = "stackoverflow"
DOC_TYPE = "questions"

result = es.search(index=INDEX,
          doc_type=DOC_TYPE,
          body = {
              'query' : {
                  'bool' : {
                      'must' : {
                          'match' : {'title' : 'django'}
                      }
                  }
              }
          })

print(result)