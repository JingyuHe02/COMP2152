import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def save_game(filename, hero, monsters_killed):
    with open(filename, 'w') as f:
        f.write(f"{hero.health_points},{hero.combat_strength}\n")
        f.write(f"{monsters_killed}\n")
    print("Game saved!")

def load_game(filename, hero):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            hp, cs = map(int, lines[0].strip().split(','))
            hero.health_points = hp
            hero.combat_strength = cs
            monsters_killed = int(lines[1].strip())
        print("Game loaded!")
        return monsters_killed
    except FileNotFoundError:
        print("No saved game found.")
        return 0

def dream_levels():
    try:
        level = int(input("Enter a dream level (0-3): "))
        if 0 <= level <= 3:
            print(f"Dream level {level} accepted.")
        else:
            print("Invalid number! Must be between 0 and 3.")
    except ValueError:
        print("Please enter a valid integer between 0 and 3.")

