import mysql.connector

class MySQLHandler:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.conn.cursor()

    def query(self, query, params=None):
        self.cur.execute(query, params or ())
        return self.cur.fetchall()

    def insert(self, table, data_dict):
        columns = ', '.join(data_dict.keys())
        placeholders = ', '.join(['%s'] * len(data_dict))
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.cur.execute(query, list(data_dict.values()))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

# pip install mysql-connector-python

# Create an instance of the MySQLHandler class
handler = MySQLHandler(host='localhost', user='your_username', password='your_password', database='your_database')

# Run a query
print(handler.query("SELECT * FROM your_table"))

# Insert data
data = {
    'column1': 'value1',
    'column2': 'value2',
    # ...
}
handler.insert('your_table', data)

# Close the connection
handler.close()
