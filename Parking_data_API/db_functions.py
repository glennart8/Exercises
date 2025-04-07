import duckdb

# python -m venv venv
# venv/Scripts/Activate

def create_database():
    con = duckdb.connect("stockholm_parking.duckdb")
    # Skapa schema 'staging' och tabellen 'parking_data' om de inte finns
    con.execute("""
    CREATE SCHEMA IF NOT EXISTS staging;
    CREATE TABLE IF NOT EXISTS staging.parking_addresses (
        time TIMESTAMP,
        address VARCHAR,
        city VARCHAR,
        price DOUBLE
    );
    """)
    return con

def insert_parking_data(con, data):
    con.execute("""
    INSERT INTO staging.parking_addresses (
        time, address, city, price
    ) VALUES (?, ?, ?, ?)
    """, (data['time'], data['address'], data['city'], data['price']))
