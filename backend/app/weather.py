import requests


class WeatherService:

    def get_weather(self, city: str):

        geo = requests.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": city,
                "count": 1
            }
        )

        geo_data = geo.json()

        if "results" not in geo_data:
            return None

        latitude = geo_data["results"][0]["latitude"]
        longitude = geo_data["results"][0]["longitude"]

        weather = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,weather_code"
            }
        )

        return weather.json()
        