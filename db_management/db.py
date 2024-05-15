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

    def execute_sql_query_and_return_data(self, sql_query: str):
        data = self.cursor.execute(sql_query)
        return data.fetchall()

    def drop_table(self, table: str):
        sql_query = f"DROP TABLE IF EXISTS {table};"
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_transmission_table(self, **kwargs):
        transmission = kwargs.get('transmission', '5 gears')
        transmission_type = kwargs.get('transmission_type', 'Automatic')

        sql_query = f"""
        INSERT INTO transmission (transmission, transmission_type) 
        VALUES ("{transmission}", "{transmission_type}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def read_data_from_table(self, table: str):
        sql_query = f'select * from {table};'
        return self.execute_sql_query_and_return_data(sql_query=sql_query)

    def update_value_in_table(self, data: dict):
        """UPDATE Customers
        SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
        WHERE CustomerID = 1;
        """
        set_value = 'SET'
        for key, value in data['values'].items():
            set_value += f' {key} = "{value}",'
        set_value = set_value[:-1]

        sql_query = f"""
        UPDATE {data['table']}
        {set_value}
        {data['where']};
        """
        self.execute_sql_query(sql_query=sql_query)

    def delete_rows_from_table(self, data: dict):
        pass

    def close_connection(self):
        self.connection.close()
