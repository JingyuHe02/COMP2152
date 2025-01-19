import random


def get_weapon_roll():

    while True:
        try:
            print("Press enter to roll the dice...")
            input()
            return random.randint(1, 6)
        except Exception as e:
            print("An error occurred:", str(e))


def get_weapon_name(weapon_roll, weapons):

    return weapons[weapon_roll - 1]  # subtract 1 because array indices start at 0


def main():
    # Define the array of weapon names
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

    # Roll the dice
    weapon_roll = get_weapon_roll()
    print(f"You rolled a {weapon_roll}")

    # Save the roll in a variable called weaponRoll and add to hero's combat strength
    hero_combat_strength = weapon_roll

    # Use the roll as an index into the weapons array
    hero_weapon = get_weapon_name(weapon_roll, weapons)

    print(f"Your chosen weapon is: {hero_weapon}")

    # Define the conditions
    if weapon_roll <= 2:
        print("You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("Your weapon is meh")
    else:
        print("Nice weapon, friend! ")

    # Check if the rolled weapon is not a Fist
    if hero_weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

    print(f"Your combat strength is: {hero_combat_strength}")


if __name__ == "__main__":
    main()

