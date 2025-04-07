# python -m venv ./env  
# .\env\Scripts\Activate.ps1
# uv pip install dlt duckdb
    
from dotenv import load_dotenv
import os
import requests
import dlt
import duckdb
import datetime
from database_functions import create_duckdb_database, insert_weather_data_to_duckdb  # Importera funktionerna

# Ladda miljövariabler från .env
load_dotenv()

# API-nyckel
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# URL-template för att hämta väderdata från OpenWeather API
url_template = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Skapa en DLT pipeline
pipeline = dlt.pipeline(destination="duckdb", dataset_name="weather_data")

# Lista på städer vi vill hämta väderdata för
cities = ['Stockholm', 'London', 'Paris', 'New York', 'Tokyo']

# --- API --
# Funktion för att hämta väderdata från OpenWeather API
def get_weather_data(city):
    url = url_template.format(city=city, api_key=WEATHER_API_KEY)
    response = requests.get(url)
    if response.status_code == 200: #  200 = att det lyckas
        return response.json()
    else:
        return None

# --- Funktion för att extrahera relevant väderinformation ---
def extract_weather_info(city, data):
    return {
        "city": city,
        "timestamp": datetime.datetime.now().isoformat(),  # Hämta aktuell tidsstämpel
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "pressure": data['main']['pressure'],
        "weather_description": data['weather'][0]['description'],
        "wind_speed": data['wind']['speed'],
        "cloudiness": data['clouds']['all']
    }

# --- DUCKDB 
# Huvudfunktion för att hämta data och ladda till DuckDB
def load_weather_data():
    # Anropa funktion och anslut till DuckDB
    con = create_duckdb_database()

    for city in cities:
        data = get_weather_data(city)
        if data:
            # Extrahera relevant väderinformation
            weather_info = extract_weather_info(city, data)
            # Lägg till väderdata till DuckDB
            insert_weather_data_to_duckdb(con, weather_info)
    # Stäng anslutningen till DuckDB
    con.close()

def check_data_in_duckdb():
    # Use context manager to ensure connection is closed after block execution
    with duckdb.connect("weather.duckdb") as con:
        # Query the database to check if data has been inserted into the table
        result = con.execute("SELECT * FROM staging.weather_by_city").fetchall()
        # Print each row of the result
        for row in result:
            print(row)




# Funktion för att hämta väderdata och endast extrahera temperaturen
# def get_temperature(city):
#     url = url_template.format(city=city, api_key=WEATHER_API_KEY)
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         temperature = data['main']['temp']
#         return temperature
#     else:
#         return None
    
if __name__ == "__main__":
    load_weather_data()
    check_data_in_duckdb()
    
    # weather_data_göteborg = get_weather_data("Göteborg")
    
    # --- Hämta temperaturen för Stockholm
    # temperature_stockholm = get_temperature("Stockholm")
    # print(f"Temperature in Stockholm: {temperature_stockholm} °C")
    
    # weather_data_stockholm = get_weather_data("Stockholm")
    # print(weather_data_stockholm.keys()) 
    # dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod'])
    
    # --plocka ut main från json
    # print(weather_data_stockholm['main'].keys()) # Endast keysen och inga values
    # print(weather_data_stockholm['main'])
    # print(weather_data_göteborg['main'])
    
    # --- Hämta väderdata för varje stad och skriv ut det
    # for city in cities:
    #     data = get_weather_data(city)
    #     if data:
    #         print(f"Weather data for {city}:")
    #         print(data)
    #     else:
    #         print(f"Failed to retrieve data for {city}")
    