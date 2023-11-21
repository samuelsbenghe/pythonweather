import internal.openweathermap.types as owm_types
import requests


class Client:
    def __init__(self, token: str):
        self.token = token

    def get_data(self, city: str) -> owm_types.WeatherData:
        latitude, longitude = get_latitude_longitude(token=self.token, city=city)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.token}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            return owm_types.WeatherData(data=data)
        except Exception as e:
            print(str(e))


def get_latitude_longitude(token: str, city: str) -> tuple:
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={token}'
    try:
        response = requests.get(url)
        data = response.json()
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    except Exception as e:
        print(str(e))
