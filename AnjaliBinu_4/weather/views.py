import requests 
from django.shortcuts import render

def forecast(request):
    city = request.GET.get('city', 'London') # Defaults to London if empty    
    url = "https://api.openweathermap.org/data/2.5/weather"    
    params = {
        'q': city,
        'appid': os.getenv('OPENWEATHER_API_KEY'),  # Use environment variable for API key
        'units': 'metric' 
    }    
    response = requests.get(url, params=params)    
    weather_data = None
    error_message = None
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'city': data.get('name'),
            'temperature': data.get('main', {}).get('temp'),
            'description': data.get('weather', [{}])[0].get('description'),
            'humidity': data.get('main', {}).get('humidity'),
            'wind_speed': data.get('wind', {}).get('speed'),
        }
    else:
        error_message = "City not found!"
    context = {
        'weather': weather_data,
        'error_message': error_message
    }
    return render(request, 'weather/forecast.html', context)