class RecommenderSystem:
    def __init__(self, items, user_preferences):
        self.items = items
        self.user_preferences = user_preferences

    def calculate_utility(self, item):
        # Basic utility function based on preferences
        utility = 0
        for feature, weight in self.user_preferences.items():
            if feature in item:
                utility += weight * item[feature]
        return utility

    def recommend(self, top_n=3):
        utilities = [(self.calculate_utility(item), item["name"]) for item in self.items]
        utilities.sort(reverse=True)  # Sort by utility
        return utilities[:top_n]


# Example items
items = [
    {"name": "Laptop", "price": 1000, "performance": 9},
    {"name": "Tablet", "price": 500, "performance": 7},
    {"name": "Smartphone", "price": 800, "performance": 8}
]

# Example user preferences (higher weight = more important)
user_preferences = {
    "price": -1,  # Prefer cheaper items
    "performance": 2  # Higher performance is better
}

recommender = RecommenderSystem(items, user_preferences)
recommendations = recommender.recommend()
print("Recommendations:", recommendations)
