from fastapi import APIRouter

from app.services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

service = AIService()


@router.get("/itinerary")
def generate_itinerary(
    destination: str,
    days: int,
    budget: float,
):
    return service.generate_itinerary(
        destination,
        days,
        budget,
    )