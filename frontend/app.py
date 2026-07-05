import csv
import io
import json
import requests
import streamlit as st
from datetime import datetime

API_URL = "http://127.0.0.1:8000"


def generate_itinerary(destination, start_date, end_date, budget):
    try:

        days = (
            datetime.fromisoformat(end_date)
            - datetime.fromisoformat(start_date)
        ).days + 1

        response = requests.get(
            f"{API_URL}/ai/itinerary",
            params={
                "destination": destination,
                "days": days,
                "budget": budget,
            },
            timeout=60,
        )

        if response.status_code == 200:
            return response.json()["itinerary"]

        return f"AI Error: {response.text}"

    except Exception as e:
        return str(e)


st.set_page_config(
    page_title="SmartTrip Planner",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ SmartTrip Planner")
st.caption(
    "Plan smarter trips with weather forecasts and AI-generated itineraries."
)

st.divider()

# -------------------------------------------------
# ADD TRIP
# -------------------------------------------------

st.header("➕ Add Trip")

destination = st.text_input("Destination")
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

budget = st.number_input(
    "Budget (€)",
    min_value=0.0,
    step=50.0,
)

if st.button("Save Trip"):

    response = requests.post(
        f"{API_URL}/trips/",
        json={
            "destination": destination,
            "start_date": str(start_date),
            "end_date": str(end_date),
            "budget": budget,
        },
    )

    if response.status_code == 200:
        st.success("Trip created successfully!")
        st.rerun()

    else:
        st.error(response.text)

st.divider()

# -------------------------------------------------
# MY TRIPS
# -------------------------------------------------

st.header("🌍 My Trips")

response = requests.get(f"{API_URL}/trips/")

if response.status_code == 200:

    trips = response.json()

    # ---------------- Dashboard ----------------

    total_trips = len(trips)

    total_budget = sum(
        trip["budget"] for trip in trips
    )

    average_budget = (
        total_budget / total_trips
        if total_trips > 0
        else 0
    )

    unique_destinations = len(
        set(trip["destination"] for trip in trips)
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Trips", total_trips)

    with col2:
        st.metric(
            "Total Budget",
            f"€{total_budget:.0f}"
        )

    with col3:
        st.metric(
            "Average Budget",
            f"€{average_budget:.0f}"
        )

    with col4:
        st.metric(
            "Unique Destinations",
            unique_destinations
        )

    st.divider()

    # ---------------- Search ----------------

    search = st.text_input("🔍 Search destination")

    if search:
        trips = [
            trip
            for trip in trips
            if search.lower() in trip["destination"].lower()
        ]

    # ---------------- Export JSON ----------------

    json_data = json.dumps(
        trips,
        indent=4,
        ensure_ascii=False,
    )

    st.download_button(
        label="⬇️ Download Trips (JSON)",
        data=json_data,
        file_name="trips.json",
        mime="application/json",
    )

    # ---------------- Export CSV ----------------

    csv_buffer = io.StringIO()

    writer = csv.writer(csv_buffer)

    writer.writerow(
        [
            "Destination",
            "Start Date",
            "End Date",
            "Budget",
        ]
    )

    for trip in trips:
        writer.writerow(
            [
                trip["destination"],
                trip["start_date"],
                trip["end_date"],
                trip["budget"],
            ]
        )

    st.download_button(
        label="⬇️ Download Trips (CSV)",
        data=csv_buffer.getvalue(),
        file_name="trips.csv",
        mime="text/csv",
    )

    st.divider()

    # ---------------- Trips ----------------

    if len(trips) == 0:
        st.info("No trips found.")

    for trip in trips:

        with st.container(border=True):

            st.subheader(f"✈️ {trip['destination']}")

            st.write(
                f"📅 {trip['start_date']} → {trip['end_date']}"
            )

            st.write(
                f"💰 Budget: €{trip['budget']}"
            )

            weather = requests.get(
                f"{API_URL}/weather/{trip['destination']}"
            ).json()

            if "error" not in weather:

                st.write(
                    f"🌤 {weather['weather']}"
                )

                st.write(
                    f"🌡 {weather['temperature']}°C"
                )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "✨ Generate itinerary",
                    key=f"ai_{trip['id']}",
                ):

                    itinerary = generate_itinerary(
                        trip["destination"],
                        trip["start_date"],
                        trip["end_date"],
                        trip["budget"],
                    )

                    with st.expander(
                        "📅 View AI Itinerary",
                        expanded=True,
                    ):
                        st.markdown(itinerary)

            with col2:

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{trip['id']}",
                ):

                    requests.delete(
                        f"{API_URL}/trips/{trip['id']}"
                    )

                    st.rerun()

else:

    st.error("Cannot connect to backend.")