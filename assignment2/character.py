import random

class Character:
    def __init__(self):
        self.__combat_strength = random.randint(1, 10)
        self.__health_points = random.randint(50, 100)
        print(f"{self.__class__.__name__} created with Combat Strength: {self.__combat_strength} and Health Points: {self.__health_points}")

    def __del__(self):
        print(f"The {self.__class__.__name__} object is being destroyed by the garbage collector")

    @property
    def combat_strength(self):
        return self.__combat_strength

    @combat_strength.setter
    def combat_strength(self, value):
        if value >= 0:
            self.__combat_strength = value
        else:
            print("Combat strength cannot be negative.")

    @property
    def health_points(self):
        return self.__health_points

    @health_points.setter
    def health_points(self, value):
        if value >= 0:
            self.__health_points = value
        else:
            print("Health points cannot be negative.")
