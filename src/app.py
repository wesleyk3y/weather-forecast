import os
from flask import Flask, jsonify
from weather_api import fetch_weather_forecast, format_weather_forecast
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app) 

# Get the API key from an environment variable
api_key = os.environ.get('OPENWEATHERMAP_API_KEY')

@app.route('/')
@cross_origin()
def get_weather():
    print("Received request for weather data for Auckland")
    
    # make sure API key is included
    if not api_key:
        print("API key not configured")
        return 'API key not configured', 500

    # get the weather data for Auckland
    weather_data = fetch_weather_forecast(api_key, "Auckland")
    
    print("Weather data received:", weather_data)
    
    # format the weather data
    formatted_weather_data = format_weather_forecast(weather_data)
    
    print("Formatted weather data:", formatted_weather_data)
    
    # return the formatted weather data as a JSON
    return jsonify(formatted_weather_data)

if __name__ == '__main__':
    app.run(debug=True)
