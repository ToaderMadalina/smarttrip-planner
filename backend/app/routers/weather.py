from fastapi import APIRouter

from app.services.weather_service import WeatherService

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)

service = WeatherService()


@router.get("/{city}")
def get_weather(city: str):
    return service.get_weather(city)