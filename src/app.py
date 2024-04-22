import os
from flask import Flask, jsonify
from weather_api import fetch_weather_forecast, format_weather_forecast

app = Flask(__name__)

# Get the API key from an environment variable
api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

@app.route('/weather/<location>')
def get_weather(location):
    # make sure API key is included
    if not api_key:
        return 'API key not configured', 500

    # get the weather data for the specified location
    weather_data = fetch_weather_forecast(api_key, location)
    
    # format the weather data
    formatted_weather_data = format_weather_forecast(weather_data)
    
    # return the formatted weather data as a JSON
    return jsonify(formatted_weather_data)

if __name__ == '__main__':
    app.run(debug=True)
