from internal.openweathermap import current_weather_data
import internal.openweathermap.types as owm_types
import requests
import datetime
import pandas as pd


class Weather:
    def __init__(self, token):
        self.token = token

    def current_weather_data(self):
        return current_weather_data.Client(token=self.token)


class _CurrentWeatherData:
    def __init__(self, token, city):
        self.token = token
        self.city = city

    def location(self, city):
        self.city = _Location(city=city, token=self.token)
        return self.city


class _Location:
    def __init__(self, city, token):
        self.token = token
        self.city = city
        self.geo_api_url = f'https://api.openweathermap.org/geo/1.0/direct?q={self.city}&limit=1&appid={self.token}'

    def get_data(self):
        latitude, longitude = self.get_coordinates()
        data = _get_data(latitude=latitude, longitude=longitude, token=self.token)
        return data

    def get_coordinates(self):
        response = requests.get(self.geo_api_url)
        data = response.json()
        if data:
            data = data[0]
            latitude = data['lat']
            longitude = data['lon']  #
            return latitude, longitude
        else:
            raise ValueError("Weather API Error: Could not find latitude and longitude of specified city")


def _get_data(latitude, longitude, token):
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={token}&units=metric"
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
                'pressure': data['main']['pressure'],
                'humidity': data['main']['humidity'],
                'visibility': data['visibility'],
                'wind': {
                    'speed': data['wind']['speed'],
                    'deg': data['wind']['deg'],
                },
                'clouds': {
                    'all': data['clouds']['all']
                },
                'rain': {
                    '1h': data['rain']['1h'] if 'rain' in data else 0,
                    '3h': data['rain']['3h'] if 'rain' in data else 0,
                },
                'snow': {
                    '1h': data['snow']['1h'] if 'snow' in data else 0,
                    '3h': data['snow']['3h'] if 'snow' in data else 0,
                },
            },
            'date': {
                'date': pd.Timestamp(datetime.datetime.fromtimestamp(data['dt'])).date(),
                'time': pd.Timestamp(datetime.datetime.fromtimestamp(data['dt'])).time(),
            },
            'timezone': data['timezone'],
        }
        return owmtypes.WeatherData(_weather_data)
    else:
        raise ValueError("Weather API Error: Weather data not found")


def extract_time_from_timestamp(timestamp):
    return pd.Timestamp(datetime.datetime.fromtimestamp(timestamp)).time()
