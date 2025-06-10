

LOCATION_TABLE_CREATION = '''CREATE TABLE IF NOT EXISTS locations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    elevation_m REAL
)
'''
Locations_Data_Query = '''INSERT INTO locations (name, latitude, longitude)
VALUES 
  ('Coimbatore', 11,77),
  ('Bengaluru', 13, 77.5),
  ('Delhi', 28.6,77.2),
  ('Chennai', 13.1,80.2);'''

LOCATION_TABLE_SELECT_QUERY = '''SELECT name, latitude, longitude FROM locations;'''


TABLE_QUERY = '''CREATE TABLE {location} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT NOT NULL,
    temperature REAL,
    humidity REAL,
    windspeed REAL,
    winddirection REAL,
    rain REAL,
    showers REAL,
    is_day BOOLEAN,
    max_temperature REAL,
    min_temperature REAL,
    ux_index_max REAL
);'''

# db_con.execute_query('DROP TABLE IF EXISTS Coimbatore;')
# Delhi          Bengaluru    Coimbatore      Chennai

TABLE_INSERT_QUERY = '''INSERT INTO {table} (time,temperature,humidity,windspeed,winddirection,rain,showers,is_day,max_temperature,
                        min_temperature,ux_index_max)  VALUES ('{time}',{temperature},{humidity},{windspeed},{winddirection},
                        {rain},{showers},{is_day},{max_temperature},{min_temperature},{ux_index_max})'''

API = '''https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=uv_index_max,sunrise,sunset,temperature_2m_max,temperature_2m_min&current=temperature_2m,relative_humidity_2m,wind_speed_10m,rain,wind_direction_10m,showers,is_day'''