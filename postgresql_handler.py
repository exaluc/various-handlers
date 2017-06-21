# Import the necessary modules
import psycopg2
from psycopg2 import sql

# Define the PostgresHandler class
class PostgresHandler:
    def __init__(self, dbname, user, password, host='localhost', port=5432):
        self.conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cur = self.conn.cursor()

    def query(self, query, params=None):
        self.cur.execute(query, params or ())
        return self.cur.fetchall()

    def insert(self, table, data_dict):
        columns = data_dict.keys()
        values = data_dict.values()
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() * len(columns))
        )
        self.cur.execute(query, values)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

# Create an instance of the PostgresHandler class
handler = PostgresHandler(dbname='your_dbname', user='your_user', password='your_password')

# Perform a query
result = handler.query('SELECT * FROM your_table')
print(result)  # prints the result of the query

# Insert data
data = {
    'column1': 'value1',
    'column2': 'value2',
    # ...
}
handler.insert('your_table', data)

# Close the connection
handler.close()
