# use unittest

import unittest
from unittest.mock import MagicMock
from weather_api import fetch_weather_forecast, format_weather_forecast

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.mock_response = MagicMock()
        self.mock_response.json.return_value = {
            "main": {"temp": 20.5, "humidity": 70},
            "weather": [{"description": "Clear sky"}],
            "wind": {"speed": 5.0}
        }
        
    def test_fetch_weather_forecast(self):
        with unittest.mock.patch('requests.get', return_value=self.mock_response):
            # dummy API key and location
            weather_data = fetch_weather_forecast('dummy_api_key', 'dummy_location')

            # check if function returns the expected data
            self.assertEqual(weather_data, self.mock_response.json.return_value)
        
    def test_format_weather_forecast(self):
        # sample weather data
        sample_data = {
            "main": {"temp": 20.5, "humidity": 70},
            "weather": [{"description": "Clear sky"}],
            "wind": {"speed": 5.0}
        }

        # Call the format_weather_data function with the sample data
        formatted_data = format_weather_forecast(sample_data)

        # Check if the function returns the expected formatted data
        expected_data = {
            "temperature": 20.5,
            "description": "Clear sky",
            "humidity": 70,
            "wind_speed": 5.0
        }
        self.assertEqual(formatted_data, expected_data)
        
        
if __name__ == '__main__':
    unittest.main()