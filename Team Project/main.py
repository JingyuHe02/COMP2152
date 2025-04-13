import os
import platform
import random
from hero import Hero
from monster import Monster
from weather import WeatherSystem
from functions import roll_dice, save_game, load_game, dream_levels

def print_system_info():
    print(f"Python version: {platform.python_version()}")
    print(f"Operating System: {os.name}")

def initialize_game():
    weather_system = WeatherSystem()
    weather_system.update_weather()

    hero = Hero()
    monster = Monster()

    weather_system.apply_weather_effects(hero)
    weather_system.apply_weather_effects(monster)

    return hero, monster, weather_system

def battle_sequence(hero, monster, weather_system):
    print("\n=== BATTLE START ===")
    print(f"Hero stats - HP: {hero.health_points}, Attack: {hero.combat_strength}")
    print(f"Monster stats - HP: {monster.health_points}, Attack: {monster.combat_strength}")

    hero.hero_attacks(monster)
    if monster.health_points > 0:
        monster.monster_attacks(hero)

    if random.random() < 0.3:
        weather_system.update_weather()
        weather_system.apply_weather_effects(hero)
        weather_system.apply_weather_effects(monster)

def main():
    print_system_info()
    hero, monster, weather_system = initialize_game()

    battle_sequence(hero, monster, weather_system)

    save_game("save.txt", hero, 5)
    print("Loaded game result:", load_game("save.txt", hero))

    dream_levels()

if __name__ == "__main__":
    main()