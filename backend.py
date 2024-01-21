
import requests
import os
from dotenv import load_dotenv
from database import create_tables, add_temperature, get_data_from_database

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_weather_data(place, forecast_days=None):
    # Ensure the database table is created
    create_tables()

    # Check if data already exists in the database
    db_data = get_data_from_database(place, forecast_days)

    if db_data:
        return db_data
        
 # Make a GET request to the API and retrieve JSON data
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
 #Filter data received depending on forecast_days input
    filtered_data = data["list"]
    nb_values = 8 * forecast_days
    filtered_data = filtered_data[:nb_values]

    # Transform and add the API data to the database
    for record in filtered_data:
        add_temperature(place, record["main"]["temp"], record["dt_txt"])

    return filtered_data




