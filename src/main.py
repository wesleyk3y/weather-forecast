from weather_api import fetch_weather_forecast, format_weather_forecast

def main():
    api_key = '809c0d51ea0065551adce85fbc3fc3c1'
    location = 'Auckland'

    # get the weather data and format it
    weather_data = fetch_weather_forecast(api_key, location)
    formatted_weather_data = format_weather_forecast(weather_data)

    # display the weather data
    print("Weather Forecast:")
    print(f"Temperature: {formatted_weather_data['temperature']}°C")
    print(f"Description: {formatted_weather_data['description']}")
    print(f"Humidity: {formatted_weather_data['humidity']}%")
    print(f"Wind Speed: {formatted_weather_data['wind_speed']} m/s")

if __name__ == "__main__":
    main()
