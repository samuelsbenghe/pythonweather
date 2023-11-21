import internal.openweathermap as owm


def main():
    weather_service = owm.Weather("3b0b63e5af21bd69a76d77b43d247827")
    current_weather_data_client = weather_service.current_weather_data()

    city = input("Enter city name: ")
    city_current_weather = current_weather_data_client.get_data(city=city)

    print(city_current_weather.location().sunset())


if __name__ == "__main__":
    main()
