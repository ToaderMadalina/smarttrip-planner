from pydantic import BaseModel


class TripBase(BaseModel):
    destination: str
    start_date: str
    end_date: str
    budget: float


class TripCreate(TripBase):
    pass


class TripUpdate(TripBase):
    pass


class TripResponse(TripBase):
    id: int

    class Config:
        from_attributes = True