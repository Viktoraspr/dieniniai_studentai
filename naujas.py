

class DB:
    def __init__(self, url):
        self.url = 'a'

    def __connect_to_db(self):
        return 0

    def __excecute_query(self, sql_query):
        pass

    def drop_table(self, table:str):
        sql_query = f'drob {table}'
        self.excecute_query(sql_query)

    def run_query(self, query):
        self.__excecute_query(query)

    def add_data_to_table_car(self, **kwargs):
        sql = f'SELECT * FROM {} WHERE pavarde = ieskomapavarde'
        ...

    def delete_data_to_table_car(self, **kwargs):
        ...
        # eilutes_value
        # paduotas_id
