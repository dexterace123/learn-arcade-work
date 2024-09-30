"""
This is lab_04.  My version of Camel.
"""
import random

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")
    print()

    # Initialize variables
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    native_distance = -20
    canteen = 3

    # Game Loop
    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print()
        user_choice = input("What is your choice? ")
        if user_choice.upper() == "Q":
            done = True
            print("Thanks for playing!")
        elif user_choice.upper() == "E":
            print()
            print("Miles traveled: ", miles_traveled)
            print("Drinks in canteen: ", canteen)
            print("The natives are", miles_traveled - native_distance, "miles behind you.")
            print()
        elif user_choice.upper() == "D":
            camel_tiredness = 0
            print()
            print("The camel is happy.")
            print()
            native_distance += random.randrange(7, 15)
        elif user_choice.upper() == "C":
            miles = random.randrange(10, 21)
            print()
            print("You traveled", miles, "miles.")
            print()
            miles_traveled += miles
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            native_distance += random.randrange(7, 15)
            if random.randrange(0, 20) == 0:
                print("You found an oasis!")
                print()
                thirst = 0
                canteen = 3
                camel_tiredness = 0
        elif user_choice.upper() == "B":
            miles = random.randrange(5, 13)
            print()
            print("You traveled", miles, "miles.")
            print()
            miles_traveled += miles
            thirst += 1
            camel_tiredness += 1
            native_distance += random.randrange(7, 15)
            if random.randrange(0, 20) == 0:
                print("You found an oasis!")
                print()
                thirst = 0
                canteen = 3
                camel_tiredness = 0
        elif user_choice.upper() == "A":
            if canteen > 0:
                canteen -= 1
                thirst = 0
            else:
                print()
                print("Your canteen is empty!")
                print()

        # Check for bad things
        if thirst>6:
            print()
            print("You died of thirst!")
            done = True
        elif thirst>4:
            print()
            print("You are thirsty.")
            print()
        if camel_tiredness>8 and not done:
            print()
            print("Your camel is dead.")
            done = True
        elif camel_tiredness>5 and not done:
            print()
            print("Your camel is getting tired.")
            print()
        if miles_traveled - native_distance <= 0 and not done:
            print()
            print("The natives have caught up to you!")
            done = True
        elif miles_traveled - native_distance < 15 and not done:
            print()
            print("The natives are getting close.")
            print()

        # Check for winning game
        if miles_traveled >= 200 and not done:
            print()
            print("You made it across the desert! You won!")
            done = True

main()
