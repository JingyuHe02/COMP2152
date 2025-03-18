import random
import sys

# Define attack functions
def hero_attacks(combat_strength, m_health_points):
    damage = combat_strength
    m_health_points -= damage
    if m_health_points < 0:
        m_health_points = 0
    print(f"Hero attacks! Monster's health is now {m_health_points}")
    return m_health_points

def monster_attacks(m_combat_strength, health_points):
    damage = m_combat_strength
    health_points -= damage
    if health_points < 0:
        health_points = 0
    print(f"Monster attacks! Hero's health is now {health_points}")
    return health_points

# Game Flow
small_dice_options = list(range(1, 7))  # Max combat strength is 6
big_dice_options = list(range(1, 21))  # Max health points is 20

# Input validation
max_attempts = 5
i = 0
input_valid = False
m_input_valid = False

while not input_valid and i < max_attempts:
    try:
        combat_strength = input("Enter your combat Strength (1-6): ")
        if not combat_strength.isnumeric():
            print("One or more invalid inputs. Player needs to enter integer numbers for Combat Strength")
        elif int(combat_strength) not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
        else:
            input_valid = True
    except ValueError:
        print("Exception: Invalid input. Player needs to enter an integer number.")
    i += 1

i = 0
while not m_input_valid and i < max_attempts:
    try:
        m_combat_strength = input("Enter the monster's combat Strength (1-6): ")
        if not m_combat_strength.isnumeric():
            print("One or more invalid inputs. Monster needs to enter integer numbers for Combat Strength")
        elif int(m_combat_strength) not in range(1, 7):
            print("Enter a valid integer between 1 and 6 only")
        else:
            m_input_valid = True
    except ValueError:
        print("Exception: Invalid input. Monster needs to enter an integer number.")
    i += 1

if input_valid and m_input_valid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for player health points
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("Player rolled " + str(m_health_points) + " health points for the monster")

    # Fight loop
    while m_health_points > 0 and health_points > 0:
        input("Roll to see who attacks first (Press Enter)")
        attack_roll = random.choice(small_dice_options)
        if attack_roll % 2 != 0:
            input("You strike (Press enter)")
            m_health_points = hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                print("Monster defeated!")
                break
            input("The monster strikes (Press enter)!!!")
            health_points = monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                print("Hero defeated!")
                break
        else:
            input("The Monster strikes (Press enter)")
            health_points = monster_attacks(m_combat_strength, health_points)
            if health_points <= 0:
                print("Hero defeated!")
                break
            input("The hero strikes!! (Press enter)")
            m_health_points = hero_attacks(combat_strength, m_health_points)
            if m_health_points <= 0:
                print("Monster defeated!")
                break
else:
    print("Invalid input. Exiting the game.")
    sys.exit(1)

print("Game over. Thanks for playing!")