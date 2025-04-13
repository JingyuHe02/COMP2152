import random

class WeatherSystem:
    """Weather system that affects game characters' attributes"""

    def __init__(self):
        """Initialize weather types and their effects"""
        self.weather_types = [
            {
                "name": "Sunny",
                "effect": "Attack +10%",
                "attack_mod": 1.1,
                "hit_mod": 1.0
            },
            {
                "name": "Rainy",
                "effect": "Hit rate -20%",
                "attack_mod": 1.0,
                "hit_mod": 0.8
            },
            {
                "name": "Blizzard",
                "effect": "HP -5",
                "health_mod": -5
            }
        ]
        self.current_weather = None

    def update_weather(self):
        """Randomly select new weather"""
        self.current_weather = random.choice(self.weather_types)
        print(f"🌤 Weather changed to: {self.current_weather['name']}, Effect: {self.current_weather.get('effect', '')}")

    def apply_weather_effects(self, character):
        """Apply weather effects to character attributes"""
        if self.current_weather is None:
            print("⚠️ No weather set.")
            return

        weather_name = self.current_weather["name"]

        if weather_name == "Sunny":
            character.combat_strength = int(character.combat_strength * self.current_weather["attack_mod"])
        elif weather_name == "Rainy":
            character.hit_rate = character.hit_rate * self.current_weather["hit_mod"]
        elif weather_name == "Blizzard":
            character.health_points += self.current_weather["health_mod"]
            if character.health_points < 0:
                character.health_points = 0  # Prevent negative HP
