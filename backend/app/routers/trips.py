from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import TripCreate
from app.services.trip_service import TripService
from app.schemas import TripCreate, TripUpdate

router = APIRouter(
    prefix="/trips",
    tags=["Trips"],
)

service = TripService()


@router.post("/")
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db),
):
    return service.create_trip(trip, db)


@router.get("/")
def get_trips(
    db: Session = Depends(get_db),
):
    return service.get_all_trips(db)


@router.get("/{trip_id}")
def get_trip(
    trip_id: int,
    db: Session = Depends(get_db),
):

    trip = service.get_trip(trip_id, db)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return trip

@router.put("/{trip_id}")
def update_trip(
    trip_id: int,
    trip: TripUpdate,
    db: Session = Depends(get_db),
):

    updated_trip = service.update_trip(trip_id, trip, db)

    if not updated_trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return updated_trip 
    
@router.delete("/{trip_id}")
def delete_trip(
    trip_id: int,
    db: Session = Depends(get_db),
):

    trip = service.delete_trip(trip_id, db)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found"
        )

    return {
        "message": "Trip deleted"
    }