class WeatherData:
    def __init__(self, data):
        self.data = data
        self.location = WeatherLocationData(data['location'])
        self.weather = WeatherWeatherData(data['weather'])


class WeatherLocationData:
    def __init__(self, data):
        self.data = data
        self.city = data['city']
        self.country = data['country']
        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.sunrise = data['sunrise']
        self.sunset = data['sunset']


class WeatherWeatherData:
    def __init__(self, data):
        self.data = data
        self.main = data['main']
        self.description = data['description']
        self.temperature = data['temperature']
        self.feels_like = data['feels_like']
        self.temp_min = data['temp_min']
        self.temp_max = data['temp_max']