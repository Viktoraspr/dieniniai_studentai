import sqlite3

from db_management.sql_queries_create_tables import URL


class DB:
    def __init__(self, url=URL):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def execute_sql_query(self, sql_query: str):
        self.cursor.execute(sql_query)
        self.connection.commit()

        print('Query executed')

    def drop_table(self, table: str):
        sql_query = f"DROP TABLE IF EXISTS {table};"
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_transmission_table(self, **kwargs):
        #   {'transmission': '5 gears', 'transmission_type': 'Manual',},
        transmission = kwargs.get('transmission', '5 gears')
        transmission_type = kwargs.get('transmission_type', 'Automatic')

        sql_query = f"""
        INSERT INTO transmission (transmission, transmission_type) 
        VALUES ("{transmission}", "{transmission_type}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def close_connection(self):
        self.connection.close()
