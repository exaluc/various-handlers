from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, host='localhost', port=27017, db_name='my_database'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]

    def insert_one(self, collection, document):
        result = self.db[collection].insert_one(document)
        return result.inserted_id

    def find(self, collection, query=None):
        results = self.db[collection].find(query or {})
        return list(results)

    def update_one(self, collection, query, new_values):
        result = self.db[collection].update_one(query, {'$set': new_values})
        return result.modified_count

    def delete_one(self, collection, query):
        result = self.db[collection].delete_one(query)
        return result.deleted_count

# Create an instance of the MongoDBHandler class
handler = MongoDBHandler(host='localhost', port=27017, db_name='test_db')

# Insert a document
doc = {
    'name': 'John',
    'email': 'john@example.com',
    'age': 27
}
print(handler.insert_one('test_collection', doc))

# Query data
query = {'age': {'$gt': 25}}
print(handler.find('test_collection', query))

# Update a document
query = {'name': 'John'}
new_values = {'email': 'john.doe@example.com'}
print(handler.update_one('test_collection', query, new_values))

# Delete a document
query = {'name': 'John'}
print(handler.delete_one('test_collection', query))
