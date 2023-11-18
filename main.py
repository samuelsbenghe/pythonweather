from internal.weather import Weather


def print_weather(data):
    print("")
    print(f"City: {data['location']['city']}")
    print(f"Country: {data['location']['country']}")
    print(f"Latitude: {data['location']['latitude']} | Longitude: {data['location']['longitude']}")
    print(f"Sunrise: {data['location']['sunrise']} | Sunset: {data['location']['sunset']}")
    print("")
    print(f"Weather: {data['weather']['main']} | Description: {data['weather']['description']}")
    print(f"Temperature: {data['weather']['temperature']}°C | Feels like: {data['weather']['feels_like']}°C | Min: {data['weather']['temp_min']}°C | Max: {data['weather']['temp_max']}°C")
    print("")


def start_weather_app():
    weather = Weather("3b0b63e5af21bd69a76d77b43d247827")
    city = input("(type 'exit' to quit) Name a city: ")
    if city == "exit":
        print("Goodbye!")
        exit(0)
    weather_data = weather.location(city).get_data()
    print_weather(weather_data)
    start_weather_app()


def main():
    start_weather_app()


if __name__ == "__main__":
    main()
