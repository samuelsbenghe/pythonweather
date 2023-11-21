# CURRENT WEATHER DATA API TYPES
class CurrentWeatherDataType:
    def __init__(self, data):
        self.data = data
        self.location = CurrentWeatherDataLocationType(data['location'])
        self.weather = CurrentWeatherDataWeatherType(data['weather'])

class CurrentWeatherDataLocationType:
    def __init__(self, data):