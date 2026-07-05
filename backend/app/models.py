from sqlalchemy import Column, Integer, String, Float

from app.database import Base


class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, index=True)
    destination = Column(String, nullable=False)
    start_date = Column(String)
    end_date = Column(String)
    budget = Column(Float)