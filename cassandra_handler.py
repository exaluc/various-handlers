from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

class CassandraHandler:
    def __init__(self, hosts, username, password, port=9042):
        auth_provider = PlainTextAuthProvider(username=username, password=password)
        self.cluster = Cluster(hosts, port=port, auth_provider=auth_provider)
        self.session = self.cluster.connect()

    def execute(self, query, parameters=None):
        return self.session.execute(query, parameters)

    def insert(self, table, data_dict):
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['%s'] * len(data_dict))
        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
        self.execute(query, list(data_dict.values()))

    def close(self):
        self.session.shutdown()
        self.cluster.shutdown()

cassandra_handler = CassandraHandler(['localhost'], 'cassandra', 'cassandra')

# Execute a raw CQL query
rows = cassandra_handler.execute('SELECT * FROM mykeyspace.mytable')
for row in rows:
    print(row)

# Insert data into a table
data = {'column1': 'value1', 'column2': 'value2'}
cassandra_handler.insert('mykeyspace.mytable', data)

cassandra_handler.close()
