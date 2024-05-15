"""
CRUD operation with database
"""


import sqlite3

from db_management.sql_queries_create_tables import URL


class DB:
    def __init__(self, url=URL):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def execute_sql_query(self, sql_query: str) -> None:
        """
        Sends sql query to database
        :param sql_query: raw sql query in string format
        :return: None
        """
        self.cursor.execute(sql_query)
        self.connection.commit()
        print('SQL executed')

    def execute_sql_query_and_return_values(self, sql_query: str) -> list[tuple]:
        return self.cursor.execute(sql_query).fetchall()

    def drop_table(self, table: str) -> None:
        sql_query = f"drop table if exists {table}"
        self.execute_sql_query(sql_query=sql_query)

    def add_values_to_transmission_table(self, **kwargs) -> None:
        sql_query = f"""
        INSERT INTO transmission (transmission, transmission_type)
        VALUES ("{kwargs['transmission']}", "{kwargs['transmission_type']}");
        """
        self.execute_sql_query(sql_query=sql_query)

    def read_data_from_table(self, table: str) -> list[tuple]:
        sql_query = f"select * from {table}"
        return self.execute_sql_query_and_return_values(sql_query=sql_query)

    def update_value_in_table(self, data: dict) -> None:
        """
        UPDATE table_name
        SET column1 = value1, column2 = value2, ...
        WHERE condition;
        :param data:
        :return:
        """
        sql_query = f"UPDATE {data['table']} "

        set_line = 'SET'
        for key, value in data['values'].items():
            set_line += f' {key} = "{value}",'
        set_line = set_line[:-1]
        sql_query += f'{set_line}  {data["where"]};'
        self.execute_sql_query(sql_query=sql_query)

    def delete_rows_from_table(self, data: dict) -> None:
        sql_query = f"""
        DELETE FROM {data['table']} 
        WHERE {data['column_name']} in {data['column_values']};
        """
        self.execute_sql_query(sql_query=sql_query)

    def close_connection(self):
        self.connection.close()
