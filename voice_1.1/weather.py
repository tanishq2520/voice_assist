import requests
from ss import key2

def get_weather_data():
    api_address = f"http://api.openweathermap.org/data/2.5/weather?q=Sonipat&appid={key2}"
    
    try:
        response = requests.get(api_address)
        response.raise_for_status()
        json_data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

    return json_data

def temp(json_data):
    if json_data:
        try:
            temperature = round(json_data['main']['temp'] - 273.15, 2)
            return temperature
        except KeyError:
            return "Temperature data not available"
    return "No data"

def des(json_data):
    if json_data:
        try:
            description = json_data['weather'][0]['description']
            return description
        except KeyError:
            return "Weather description not available"
    return "No data"

json_data = get_weather_data()
