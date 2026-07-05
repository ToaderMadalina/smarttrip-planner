# ✈️ SmartTrip Planner

SmartTrip Planner is a Python web application that helps users organize their trips by combining trip management, weather forecasts, and AI-generated travel itineraries.

The project was developed using **FastAPI** for the backend and **Streamlit** for the frontend.

---

# Features

- ✅ Create, update and delete trips
- 🌍 Manage multiple travel destinations
- 🌤 Live weather forecast using Open-Meteo API
- 🤖 AI-generated travel itineraries
- 🔍 Search trips by destination
- 📊 Dashboard with travel statistics
- 📥 Export trips to JSON
- 📥 Export trips to CSV
- 📝 Application logging

---

# Technologies Used

## Backend

- Python 3.10
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Requests

## Frontend

- Streamlit

## External APIs

- Open-Meteo Weather API
- Google Gemini API (with fallback itinerary generation)

---

# Project Structure

```
smarttrip-planner
│
├── backend
│   ├── app
│   │   ├── routers
│   │   ├── services
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── database.py
│   │   ├── logger.py
│   │   └── main.py
│   ├── logs
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   └── app.py
│
└── README.md
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/ToaderMadalina/smarttrip-planner.git
cd smarttrip-planner
```

---

## 2. Backend

```bash
cd backend

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

## 3. Frontend

Open another terminal:

```bash
cd frontend

streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

# Application Workflow

1. Add a trip.
2. Store the trip in SQLite.
3. Display all trips.
4. Retrieve the current weather.
5. Generate an AI itinerary.
6. Export trips as JSON or CSV.

---

# Dashboard

The application provides travel statistics including:

- Total Trips
- Total Budget
- Average Budget
- Unique Destinations

---

# Logging

Application events are stored in:

```
backend/logs/app.log
```

Examples:

```
INFO | Trip created: Berlin
INFO | Weather requested for Berlin
INFO | AI itinerary generated for Berlin
INFO | Trip deleted: Berlin
```

---

# API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/trips` | Get all trips |
| GET | `/trips/{id}` | Get trip by ID |
| POST | `/trips` | Create trip |
| PUT | `/trips/{id}` | Update trip |
| DELETE | `/trips/{id}` | Delete trip |
| GET | `/weather/{city}` | Get weather |
| GET | `/ai/itinerary` | Generate itinerary |

---

# Future Improvements

- User authentication
- Interactive maps
- Hotel recommendations
- Flight price integration
- PDF itinerary export
- Email notifications

---

# Author

**Mădălina Toader**

SmartTrip Planner – Python Final Project