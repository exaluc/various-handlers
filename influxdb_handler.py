from influxdb import InfluxDBClient

class InfluxDBHandler:
    def __init__(self, host='localhost', port=8086, user='root', password='root', dbname=None):
        self.client = InfluxDBClient(host, port, user, password, dbname)

    def create_db(self, dbname):
        self.client.create_database(dbname)

    def switch_db(self, dbname):
        self.client.switch_database(dbname)

    def insert_data(self, json_body):
        self.client.write_points(json_body)

    def query_data(self, query):
        result = self.client.query(query)
        return result.raw

    def close(self):
        self.client.close()

handler = InfluxDBHandler(dbname='mydb')

# Create a new database
handler.create_db('mydb')

# Switch to the new database
handler.switch_db('mydb')

# Insert some data
json_body = [
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]
handler.insert_data(json_body)

# Query some data
print(handler.query_data('SELECT "value" FROM "cpu_load_short" WHERE "region"="us-west"'))

handler.close()
