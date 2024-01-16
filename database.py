import sqlite3

# Establish connection to SQLite database
def get_connection():
    return sqlite3.connect('data.db', check_same_thread=False)

# Main SQL queries
CREATE_TEMPERATURES_TABLE = '''CREATE TABLE IF NOT EXISTS weather_data (
    Place TEXT,
    Temperature REAL,
    Timestamp TEXT
)'''

INSERT_TEMPERATURE = "INSERT INTO weather_data (Place, Temperature, Timestamp) VALUES (?, ?, ?);"

SELECT_TEMPERATURES = "SELECT * FROM weather_data WHERE Place = ? LIMIT ?;"

def create_tables():
    with get_connection() as connection:
        connection.execute(CREATE_TEMPERATURES_TABLE)

def add_temperature(place, temperature, timestamp):
    with get_connection() as connection:
        connection.execute(INSERT_TEMPERATURE, (place, temperature, timestamp))

def get_data_from_database(place, limit):
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_TEMPERATURES, (place, limit))
        return list(cursor.fetchall())
