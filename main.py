import sqlite3

from db_management.sql_queries_create_tables import TABLES, DROP_TABLES
from db_management.table_data import TRANSMISSION_DATA

# CRUD

connection = sqlite3.connect("database/mano_duomenu_baze.db")
cursor = connection.cursor()

from db_management.db import DB

db = DB()

# for table in DROP_TABLES:
#     db.drop_table(table=table)
#
# for table_query in TABLES:
#     db.execute_sql_query(table_query)

for data in TRANSMISSION_DATA:
    db.add_values_to_transmission_table(**data)

db.close_connection()
