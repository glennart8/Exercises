from dotenv import load_dotenv
import os
import dlt
import requests
import datetime
from db_functions import create_database, insert_parking_data 

# 1. Installera nödvändiga bibliotek
# 2. Skapa en .env-fil med din API-nyckel
# 3. Skapa en databas med DuckDB
# 4. Skapa en pipeline med DLT
# 5. Hämta data från API:et och formatera den
# 6. Ladda den formaterade datan till databasen
# 7. Kör skriptet
# 8. Kontrollera databasen för att se om datan har laddats korrekt

# 9. Om du vill schemalägga skriptet, använd en schemaläggare som cron eller Windows Task Scheduler



load_dotenv() #Hämtar API-nyckeln från .env-filen
url = "https://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/weekday/måndag" 
pipeline = dlt.pipeline(destination="duckdb", dataset_name="parking_data") # Skapa en DLT-pipeline för att ladda data till DuckDB

# Funktion för att hämta parkeringsdata från API:et
def get_parking_data():
    api_key = os.getenv("PARKING_API_KEY")
    
    params = {
        "maxFeatures": 10,
        "outputFormat": "json",
        "apiKey": api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status() # Inbygd funktion för att hantera fel vid API-anrop
    data = response.json() # Konvertera svaret till JSON-format
    return data # Returnerar data för att användas i nästa steg

# Funktion för att formatera parkeringsdata innan inmatning i databasen
def format_parking_data(data):
    formatted_data = [] # Skapar en tom lista för att lagra formaterad data 
    
    # Iterera över varje objekt i "features" från API-svaret
    for item in data.get("features", []): # Om "features" inte finns, returnera en tom lista
        # Försök hämta varje fält med .get() så vi inte får KeyError om nyckeln saknas
        address = item['properties'].get('ADDRESS', 'Ej angiven') # Om ingen address finns, använd en standardsträng 
        city = item['properties'].get('CITY_DISTRICT', 'Ej angiven')
        price = item['properties'].get('PARKING_RATE', 0.0)
        
        # Lägg till den formaterade datan i listan - konvertera till dictionary
        formatted_data.append({
            'time': datetime.datetime.now() ,
            'ADDRESS': address,
            'CITY_DISTRICT': city,
            'PARKING_RATE': price
        })
    # Returnera den formaterade datan för att användas i nästa steg    
    return formatted_data


def load_parking_data():
    con = create_database()
    data = get_parking_data()
    formatted_data = format_parking_data(data)

    for row in formatted_data:
        insert_parking_data(con, row)
        
    # Kontrollera att datan har laddats
    check_parking_data(con)  # Lägg till denna rad för att kontrollera om datan har laddats korrekt
        
        
def check_parking_data(con):
    result = con.execute("SELECT * FROM staging.parking_addresses ORDER BY time DESC LIMIT 10").fetchall()
    print("Dessa 10 raderna har lagts till:")
    for row in result:
        print(row)
       
       
if __name__ == "__main__":
    load_parking_data()