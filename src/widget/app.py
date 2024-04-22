from flask import Flask, jsonify
from weather_api import fetch_weather_forecast, format_weather_forecast

app = Flask(__name__)

@app.route('/weather/<location>')
def get_weather(location):
    api_key = 'YOUR_API_KEY'
    weather_data = fetch_weather_forecast(api_key, location)
    formatted_weather_data = format_weather_forecast(weather_data)
    return jsonify(formatted_weather_data)

if __name__ == '__main__':
    app.run(debug=True)
