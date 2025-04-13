import random
from functions import roll_dice


class Character:
    """Base class for all game characters (Hero and Monster)"""

    def __init__(self):
        """
        Initialize character with random combat stats
        Uses dice rolls for combat strength and health points
        """
        self._combat_strength = roll_dice()  # Attack power (1-20)
        self._health_points = roll_dice()  # Health points (1-20)
        self.hit_rate = 1.0  # Chance to hit (0.0-1.0)

    # Property getters and setters with validation
    @property
    def combat_strength(self):
        """Getter for combat strength (read-only)"""
        return self._combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        """Setter for combat strength with validation"""
        self._combat_strength = max(0, value)  # Ensure never negative

    @property
    def health_points(self):
        """Getter for health points"""
        return self._health_points

    @health_points.setter
    def health_points(self, value):
        """Setter for health points with validation"""
        self._health_points = max(0, value)  # Ensure never negative

    def __del__(self):
        """Destructor - called when object is garbage collected"""
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector.")
