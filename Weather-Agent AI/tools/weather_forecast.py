import requests
from datetime import datetime
from dotenv import load_dotenv
from langchain.tools import tool
import os


class WeatherForecastTool():

    @tool("Get weather forecast")
    def get_weather_forecast(city_name):
        """
        Get a detailed weather forecast of the city. The degree of measure in temperature must be in Celsius or Farenheit. 
        For example 20°C or 20°F. There must be a detailed report of the weather forecast of the region.
        """
        api_key = os.environ['OPENWEATHER_API_KEY']
        forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        forecast = []
        today = datetime.now().date()
        for entry in forecast_data["list"]:
            date = datetime.fromtimestamp(entry["dt"]).date()
            if date > today:
                forecast.append({
                    "date": date,
                    "description": entry["weather"][0]["description"],
                    "temperature": entry["main"]["temp"],
                    "humidity": entry["main"]["humidity"],
                    "wind_speed": entry["wind"]["speed"]
                })
                if len(forecast) == 3:
                    break

        return forecast