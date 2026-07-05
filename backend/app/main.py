from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routers import trips
from app.routers import weather
from app.routers import ai

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SmartTrip Planner API",
    description="Plan your vacations smarter with AI",
    version="1.0.0",
)

app.include_router(trips.router)
app.include_router(weather.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "Welcome to SmartTrip Planner API"}