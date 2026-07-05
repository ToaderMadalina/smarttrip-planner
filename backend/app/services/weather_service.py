import requests


class WeatherService:

    GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
    WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

    WEATHER_CODES = {
        0: "☀️ Clear sky",
        1: "🌤 Mainly clear",
        2: "⛅ Partly cloudy",
        3: "☁️ Overcast",
        45: "🌫 Fog",
        48: "🌫 Fog",
        51: "🌦 Light drizzle",
        61: "🌧 Rain",
        63: "🌧 Moderate rain",
        65: "🌧 Heavy rain",
        71: "❄️ Snow",
        80: "🌦 Rain showers",
        95: "⛈ Thunderstorm",
    }

    def get_weather(self, city: str):

        geo_response = requests.get(
            self.GEO_URL,
            params={
                "name": city,
                "count": 1
            }
        )

        geo_data = geo_response.json()

        if "results" not in geo_data:
            return {
                "error": "City not found"
            }

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_response = requests.get(
            self.WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,weather_code"
            }
        )

        weather = weather_response.json()

        return {
            "city": city,
            "temperature": weather["current"]["temperature_2m"],
            "weather": self.WEATHER_CODES.get(
                weather["current"]["weather_code"],
                "Unknown"
            )
        }