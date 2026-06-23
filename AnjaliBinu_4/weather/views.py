import requests 
from django.shortcuts import render

def forecast(request):
    city = request.GET.get('city', 'London') # Defaults to London if empty    
    # Keep the base URL clean without placeholders
    url = "https://api.openweathermap.org/data/2.5/weather"    
    params = {
        'q': city,
        'appid': '0100d0c36f882ddbed22af84632b40b0',
        'units': 'metric' # Fixed typo from 'metrics'
    }    
    response = requests.get(url, params=params)    
    weather_data = None
    error_message = None
    if response.status_code == 200:
        data = response.json()
        # Formatting the data specifically for your HTML keys
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