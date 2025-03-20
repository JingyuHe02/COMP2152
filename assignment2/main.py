import os
import platform
from hero import Hero
from monster import Monster

# Print Python version
print(f"Python version: {platform.python_version()}")

# Print operating system name
print(f"Operating System: {os.name}")

# Instantiate Hero and Monster
hero = Hero()
monster = Monster()

# Example fight sequence
hero.hero_attacks()
monster.monster_attacks()

# Save game state
def save_game(monsters_killed):
    with open("save.txt", "w") as file:
        file.write(f"Monsters Killed: {monsters_killed}\n")

# Load game state
def load_game():
    try:
        with open("save.txt", "r") as file:
            line = file.readline()
            print(line.strip())
    except FileNotFoundError:
        print("No saved game found.")

# Example usage
save_game(5)  # Save the number of monsters killed
load_game()   # Load the saved game state

# Testing try-except block for dream levels
def dream_levels():
    try:
        level = int(input("Enter dream level (0-3): "))
        if level < 0 or level > 3:
            raise ValueError("Level must be between 0 and 3.")
        print(f"Dream level set to: {level}")
    except ValueError as e:
        print(f"Invalid input: {e}")

# Test dream levels function
dream_levels()