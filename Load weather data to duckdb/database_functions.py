import duckdb

# Skapa DuckDB-databasen och anslut
def create_duckdb_database():
    con = duckdb.connect("weather.duckdb")
    # Skapa schema 'staging' och tabellen 'weather_by_city' om de inte finns
    con.execute("""
    CREATE SCHEMA IF NOT EXISTS staging;
    CREATE TABLE IF NOT EXISTS staging.weather_by_city (
        city VARCHAR,
        timestamp TIMESTAMP,
        temperature DOUBLE,
        humidity INT,
        pressure INT,
        weather_description VARCHAR,
        wind_speed DOUBLE,
        cloudiness INT
    );
    """)
    return con

# Funktion för att lägga till väderdata till DuckDB
def insert_weather_data_to_duckdb(con, data):
    con.execute("""
    INSERT INTO staging.weather_by_city (
        city, timestamp, temperature, humidity, pressure, 
        weather_description, wind_speed, cloudiness
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (data['city'], data['timestamp'], data['temperature'], 
          data['humidity'], data['pressure'], data['weather_description'], 
          data['wind_speed'], data['cloudiness']))