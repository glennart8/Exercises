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
    return con # Returnera anslutningen för att använda den senare av andra funktioner. Skulle inte kunnat användas i insert_parking_data annars t.ex.

def insert_parking_data(con, data):
    try:
        con.execute("""
        INSERT INTO staging.parking_addresses (
            time, address, city, price
        ) VALUES (?, ?, ?, ?)
        """, (data['time'], data['ADDRESS'], data['CITY_DISTRICT'], data['PARKING_RATE']))
        print(f"Data insatt: {data}")  # Bekräfta insättningen
    except Exception as e:
        print(f"Fel vid insättning av data: {e}")
        
#   Ändrade till varchar för att kunna läsa in data från API:et
#   ALTER TABLE staging.parking_addresses
#   ALTER COLUMN price TYPE VARCHAR(255);
