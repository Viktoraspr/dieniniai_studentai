URL = 'database/mano_duomenu_baze.db'

TRANSMISSION_TABLE = """
CREATE TABLE IF NOT EXISTS transmission (
transmission_id INTEGER PRIMARY KEY,
transmission char,
transmission_type char,
one_more_column char DEFAULT 0);
"""

TABLES = [TRANSMISSION_TABLE]

DROP_TABLES = ['transmission', 'engine', 'model_type', 'model', 'market']
