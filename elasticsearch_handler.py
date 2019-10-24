from elasticsearch import Elasticsearch

class ElasticsearchHandler:
    def __init__(self, host='localhost', port=9200):
        self.es = Elasticsearch([{'host': host, 'port': port}])

    def insert(self, index, doc_type, doc):
        res = self.es.index(index=index, doc_type=doc_type, body=doc)
        return res['result']

    def query(self, index, body):
        res = self.es.search(index=index, body=body)
        return res['hits']['hits']

# Create an instance of the ElasticsearchHandler class
handler = ElasticsearchHandler(host='localhost', port=9200)

# Insert a document
doc = {
    'author': 'test',
    'text': 'test',
    'timestamp': '2023-07-28'
}
print(handler.insert('test-index', 'test', doc))

# Query data
body = {
    'query': {
        'match_all' : {}
    }
}
print(handler.query('test-index', body))
