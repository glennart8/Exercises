from dotenv import load_dotenv
import os
import dlt
import requests
import datetime
from db_functions import create_database, insert_parking_data  # Importera funktionerna

load_dotenv()

url = "https://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/weekday/{WEEKDAY}?maxFeatures={MAXFEATURES}&outputFormat={FORMAT}&callback={CALLBACK}&apiKey={APIKEY}"
# URL FÖR TEST I WEBBLÄSARE - https://openparking.stockholm.se/LTF-Tolken/v1/ptillaten/weekday/1?maxFeatures=10&outputFormat=json&callback=callback&apiKey=197afd02-6cc3-4c91-9720-c4dd29ced583

# Skapa en DLT pipeline
pipeline = dlt.pipeline(destination="duckdb", dataset_name="parking_data")


def get_parking_data():
    api_key = os.getenv("PARKING_API_KEY")
    if not api_key:
        print("API-nyckel saknas eller kunde inte hämtas från miljövariabler")
    else:
        print(f"API-nyckel: {api_key[:5]}...")  # Skriv ut de första 5 tecknen för att verifiera att nyckeln finns
        
    params = {
        "WEEKDAY": "1", 
        "MAXFEATURES": 100,
        "FORMAT": "json",
        "CALLBACK": "callback",
        "APIKEY": api_key
    }
    
    response = requests.get(url, params=params) # Gör API-anropet
    
    if response.status_code == 200:
        data = response.json()
        print("API-svar mottaget:", data)  # Skriv ut hela svaret
        return data
    else:
        print(f"Fel vid API-anrop: {response.status_code}, Svar: {response.text}")  # Skriv ut fel
        return None
    
    # --- DUCKDB ---
def load_parking_data():
    # Anropa funktion och anslut till DuckDB
    con = create_database()

    # Hämta parkeringsdata
    data = get_parking_data()
    
    
if __name__ == "__main__":
    get_parking_data()
   
