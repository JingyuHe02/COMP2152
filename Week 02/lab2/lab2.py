#Define a new array called weapons and add 6 different weapon names in the array,
#with increasing levels of weapon strength. Use Fist, Knife, Club, Gun, Bomb, Nuclear bomb
#Roll the dice (1-6) to choose which weapon you must use.
#Save the roll in a variable called weaponRoll.
#Add your weaponRoll to the hero's combat strength
#Use this variable as an index into the weapons array and print out the name of the hero's weapon.
#Define the following condition:
#If weaponRoll is less than or equal to 2, print out "You rolled a weak weapon, friend".
#But if weaponRoll is less than or equal to 4, print out "Your weapon is meh"
#Else, print out "Nice weapon, friend! "
#If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
#Add error handling on all inputs eg. if input is not int, print an error message and halt

import random


def number_guessing_game():
    targetNumber = random.randrange(1, 100)
    play = input("Do you want to play number guessing game? (yes/no)").strip().lower()
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        try:
            userGuess = int(input("Enter your guess:"))
            attempts += 1

            if userGuess < targetNumber:
                if (userGuess - targetNumber) <= 5:
                    print("Too low! You are very close! Try again")
                else:
                    print("Too Low, Try Again")
            elif userGuess > targetNumber:
                if abs(userGuess - targetNumber) <= 5:
                    print("Too high! You are very close! Try again")
                else:
                    print("Too high! Try again")
            else:
                print(f"Congratulations! You've guessed it in {attempts} attempts.")
                return True
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 100")

    print(f"Game over! The target number was {targetNumber}.")
    return True

number_guessing_game()
