URL = 'database/mano_duomenu_baze.db'

TRANSMISSION_TABLE = """
CREATE TABLE IF NOT EXISTS transmission (
transmission_id INTEGER PRIMARY KEY,
transmission char,
transmission_type char);
"""

ENGINE_TABLE = """
CREATE TABLE IF NOT EXISTS engine (
engine_id INTEGER PRIMARY KEY,
engine_type char,
cc_displacement char,
power(BHP) INTEGER,
torque(NM) INTEGER,
Ful_type char);
"""


MODEL_TYPE_TABLE = """
CREATE TABLE IF NOT EXISTS model_type (
model_type_id INTEGER PRIMARY KEY,
make char,
body_type char,
seating_capacity INTEGER,
fuel_tank_capacity(L) INTEGER,
Ful_type char);

"""

MODEL_TABLE = """
CREATE TABLE IF NOT EXISTS model (
model_id INTEGER PRIMARY KEY,
car_name char,
mileage(kmpl) INTEGER,
model char,
emission INTEGER,
model_type_id INTEGER,
engine_id INTEGER,
transmission_id INTEGER);
"""

MARKET_TABLE = """
CREATE TABLE IF NOT EXISTS model (
market_id INTEGER PRIMARY KEY,
price INTEGER,
make_year INTEGER,
color char,
mileage_run char,
no_of_owners char,
model_id INTEGER);
"""


TABLES = [TRANSMISSION_TABLE]
DROP_TABLES = ['transmission', 'engine', 'model_type', 'model', 'market']
