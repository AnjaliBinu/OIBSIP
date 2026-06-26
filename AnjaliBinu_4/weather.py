import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_weather(city_name):
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Retrieve the API key from your environment variables
    api_key = os.getenv('OPENWEATHER_API_KEY')
    
    if not api_key:
        print("❌ Error: API key not found. Please check your .env file.")
        return

    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Keeps temperature in Celsius
    }

    try:
        # Fetching the data from the API
        response = requests.get(url, params=params)
        
        # Check if the status code is 200 (Success)
        if response.status_code == 200:
            data = response.json()
            
            # Extracting basic information from the JSON payload
            city = data.get('name')
            temp = data.get('main', {}).get('temp')
            humidity = data.get('main', {}).get('humidity')
            description = data.get('weather', [{}])[0].get('description')
            
            # Displaying the data cleanly in the command line
            print("\n" + "="*30)
            print(f"🌍 Weather in {city}:")
            print(f"🌡️  Temperature: {temp}°C")
            print(f"💧 Humidity: {humidity}%")
            print(f"☁️  Condition: {description.capitalize()}")
            print("="*30 + "\n")
            
        elif response.status_code == 404:
            print("❌ City not found! Please check your spelling and try again.")
        else:
            print(f"❌ Error: Received status code {response.status_code} from server.")
            
    except requests.exceptions.RequestException:
        # Handles internet loss/downtime without crashing the script
        print("❌ Network Error: Could not connect to the weather service. Check your internet connection.")

if __name__ == "__main__":
    print("🌤️  Welcome to the Command-Line Weather App 🌤️")
    user_city = input("Enter a city name or ZIP code: ").strip()
    
    if user_city:
        get_weather(user_city)
    else:
        print("❌ You must enter a location.")