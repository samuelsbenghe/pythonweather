import requests
import datetime
import pandas as pd
from internal.weather import weather_types


class Weather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.city = None
        self.weather_api_url = f''

    def location(self, city):
        self.city = _Location(city=city, api_key=self.api_key)
        return self.city


class _Location:
    def __init__(self, city, api_key):
        self.api_key = api_key
        self.city = city
        self.geo_api_url = f'https://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={self.api_key}'

    def get_data(self):
        latitude, longitude = self.get_coordinates()
        data = _get_data(latitude=latitude, longitude=longitude, api_key=self.api_key)
        return data

    def get_coordinates(self):
        response = requests.get(self.geo_api_url)
        data = response.json()
        if data:
            data = data[0]
            latitude = data['lat']
            longitude = data['lon']
            return latitude, longitude
        else:
            raise ValueError("Weather API Error: Location not found")


def _get_data(latitude, longitude, api_key):
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(weather_api_url)
    data = response.json()
    if data:
        _weather_data = {
            'location': {
                'city': data['name'],
                'country': data['sys']['country'],
                'latitude': data['coord']['lat'],
                'longitude': data['coord']['lon'],
                'sunrise': extract_time_from_timestamp(data['sys']['sunrise']),
                'sunset': extract_time_from_timestamp(data['sys']['sunset']),
            },
            'weather': {
                'main': data['weather'][0]['main'],
                'description': data['weather'][0]['description'],
                'temperature': data['main']['temp'],
                'feels_like': data['main']['feels_like'],
                'temp_min': data['main']['temp_min'],
                'temp_max': data['main']['temp_max'],
            },
        }
        class_weather_data = weather_types.WeatherData(_weather_data)  # Convert dict to class
        return class_weather_data
    else:
        raise ValueError("Weather API Error: Weather data not found")


def extract_time_from_timestamp(timestamp):
    return pd.Timestamp(datetime.datetime.fromtimestamp(timestamp)).time()
