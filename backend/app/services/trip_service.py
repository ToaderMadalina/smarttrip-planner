from sqlalchemy.orm import Session

from app.models import Trip
from app.schemas import TripCreate, TripUpdate

from app.logger import logger

class TripService:

    def get_all_trips(self, db: Session):
        return db.query(Trip).all()

    def get_trip(self, trip_id: int, db: Session):
        return db.query(Trip).filter(Trip.id == trip_id).first()

    def create_trip(self, trip: TripCreate, db: Session):
        db_trip = Trip(**trip.model_dump())

        db.add(db_trip)
        db.commit()
        db.refresh(db_trip)
        logger.info(f"Trip created: {db_trip.destination}")
        print(">>> CREATE TRIP EXECUTED <<<")

        return db_trip

    def delete_trip(self, trip_id: int, db: Session):
        trip = self.get_trip(trip_id, db)

        if not trip:
            return None

        logger.info(f"Trip deleted: {trip.destination}")
        db.delete(trip)
        db.commit()

        return trip

    def update_trip(self, trip_id: int, updated_trip: TripUpdate, db: Session):
        trip = self.get_trip(trip_id, db)

        if not trip:
            return None

        trip.destination = updated_trip.destination
        trip.start_date = updated_trip.start_date
        trip.end_date = updated_trip.end_date
        trip.budget = updated_trip.budget

        db.commit()
        db.refresh(trip)
        logger.info(f"Trip updated: {trip.destination}")

        return trip