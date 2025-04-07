from dotenv import load_dotenv
import os
import dlt
import requests
import datetime
from db_functions import create_database, insert_parking_data  # Importera funktionerna

load_dotenv()

url = "https://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/weekday/måndag"
pipeline = dlt.pipeline(destination="duckdb", dataset_name="parking_data")

def get_parking_data():
    api_key = os.getenv("PARKING_API_KEY")
    if not api_key:
        print("API-nyckel saknas eller kunde inte hämtas från miljövariabler")
        return None
    else:
        print(f"API-nyckel: {api_key[:5]}...")  # Skriv ut de första 5 tecknen för att verifiera att nyckeln finns
        
    params = {
        "maxFeatures": 10,
        "outputFormat": "json",
        "apiKey": api_key
    }
    
    print(f"Anropar URL: {url} med parametrar: {params}")
    
    try:
        response = requests.get(url, params=params)  # Gör API-anropet
        response.raise_for_status()  # Kasta fel om statuskod är annat än 2xx ISTÄLLET FÖR IF-STATEMENT
        data = response.json()
        
        print(f"API-svar mottaget: {data}")
        return data
    except requests.RequestException as e:
        print(f"Fel vid API-anrop: {e}")
        return None


def format_parking_data(data):
    # Format the API data into the structure expected by the database. INNAN DU LADDAR TILL DATABASEN
    formatted_data = []
    time = datetime.datetime.now()  # Sätt aktuell tid för inmatningen
    
    # Här antar vi att data['features'] innehåller parkeringsinformation
    for item in data.get("features", []):
        # Extrahera relevant data från API-svaret
        try:            
            # Försök hämta varje fält med .get() så vi inte får KeyError om nyckeln saknas
            address = item['properties'].get('ADDRESS', 'Ej angiven')  # Om ingen address finns, använd en standardsträng
            city = item['properties'].get('CITY_DISTRICT', 'Ej angiven')
            price = item['properties'].get('PARKING_RATE', 0.0)
            
            # Lägg till den formaterade datan i listan
            formatted_data.append({
                'time': time,
                'ADDRESS': address,
                'CITY_DISTRICT': city,
                'PARKING_RATE': price
            })
        except KeyError as e:
            print(f"Fel vid bearbetning av data: Nyckel {e} saknas i ett objekt.")
            continue
    
    return formatted_data


def load_parking_data():
    # Anropa funktion och anslut till DuckDB
    con = create_database()
    print("Databas skapad och ansluten.")

    # Hämta parkeringsdata
    data = get_parking_data()
    
    if data is None or "features" not in data:
        print("Ingen giltig parkeringsdata hämtad.")
        return
    
    # Formatera datan för att matcha den förväntade strukturen i databasen
    formatted_data = format_parking_data(data)
    
    if not formatted_data:
        print("Inget formaterad data att ladda.")
        return

    # Ladda varje rad av data till DuckDB
    for row in formatted_data:
        insert_parking_data(con, row)

    print("Slut på metoder")

if __name__ == "__main__":
    load_parking_data()  # Kör funktionen som hämtar och laddar data
