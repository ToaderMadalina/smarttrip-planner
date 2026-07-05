from app.logger import logger

class AIService:

    DESTINATIONS = {
        "barcelona": [
            "Visit Sagrada Família",
            "Walk along La Rambla",
            "Explore Park Güell",
            "Visit Casa Batlló",
            "Relax at Barceloneta Beach",
            "Discover the Gothic Quarter",
            "Enjoy tapas in El Born"
        ],
        "rome": [
            "Visit the Colosseum",
            "Explore the Roman Forum",
            "Throw a coin in Trevi Fountain",
            "Visit the Vatican Museums",
            "Walk around Piazza Navona",
            "Enjoy authentic Italian pasta",
            "Watch the sunset at Castel Sant'Angelo"
        ],
        "paris": [
            "Visit the Eiffel Tower",
            "Explore the Louvre Museum",
            "Walk through Montmartre",
            "Cruise on the Seine",
            "Visit Notre-Dame",
            "Relax in Luxembourg Gardens",
            "Enjoy French pastries"
        ]
    }

    def generate_itinerary(self, destination: str, days: int, budget: float):
        logger.info(
            f"AI itinerary generated for {destination}"
        )   
        activities = self.DESTINATIONS.get(
            destination.lower(),
            [
                "Visit the city center",
                "Explore local attractions",
                "Try traditional food",
                "Visit museums",
                "Relax in parks",
                "Go shopping",
                "Discover local culture"
            ]
        )

        budget_type = "Budget"

        if budget > 2500:
            budget_type = "Luxury"
        elif budget > 1500:
            budget_type = "Comfort"

        itinerary = []

        itinerary.append(f"# ✈️ {destination}")
        itinerary.append("")
        itinerary.append(f"**Trip length:** {days} days")
        itinerary.append(f"**Budget:** €{budget:.0f} ({budget_type})")
        itinerary.append("")

        for day in range(days):

            activity = activities[day % len(activities)]

            itinerary.append(f"## Day {day + 1}")
            itinerary.append(f"✅ {activity}")

            if budget_type == "Luxury":
                itinerary.append("🍽 Dinner at a highly rated restaurant")
                itinerary.append("🏨 Stay in a 4★ or 5★ hotel")

            elif budget_type == "Comfort":
                itinerary.append("🍽 Try a popular local restaurant")
                itinerary.append("🏨 Stay in a comfortable hotel")

            else:
                itinerary.append("🥪 Eat at local affordable places")
                itinerary.append("🏨 Stay in a budget accommodation")

            itinerary.append("")

        itinerary.append("### 💡 Travel Tips")
        itinerary.append("- Use public transport.")
        itinerary.append("- Book attractions online.")
        itinerary.append("- Keep some cash for small shops.")
        itinerary.append("- Enjoy the local cuisine!")

        return {
            "itinerary": "\n".join(itinerary)
        }