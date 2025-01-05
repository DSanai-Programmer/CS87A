'''
Dario Sanai
CS87A, Fall 2024
sanaidario@gmail.com
Project 2
'''

import random

# Name: seedRand
# Purpose: Initialize the random number generator
# Input: 1. A number with string data type
# Output: None
# Side effects: Generates a consistent set of numbers

def seedRand(userSeed):
    if userSeed != "":
        userSeed = int(userSeed)
        random.seed(userSeed)
    return

# Name: roll()
# Purpose: Returns a list of the three dice rolls
# Input: None
# Output: List of 3 integers
# Side effects: None

def roll():
    diceRolls = []
    x = 0
    while x < 3:
        diceRolls.append(random.randrange(6) + 1)
        x += 1
    return diceRolls

# Name: computeBetResult
# Purpose: Returns a single integer representing how much the user won or lost
# Input: 1. List given by the roll() function
#        2. How much the user put into the bet, in integer form
#        3. Integer 1-6
# Output: Variable representing profit or loss
# Side effects: Prints a statement telling the user how many dice they matched

def computeBetResult(diceRolls, userBet, userGuess):
    y = diceRolls.count(userGuess)
    print("You matched " + str(y) + " dice!")
    userWinnings = 0

    if y == 0:
        userWinnings = -1 * userBet
    elif y == 1:
        userWinnings = userBet
    elif y == 2:
        userWinnings = 2 * userBet
    elif y == 3:
        userWinnings = 10 * userBet
    return userWinnings


def main():
    money = 100
    goAgain = "y"
    print("STEP RIGHT UP AND PLAY SOME CHUCK-A-LUCK!")
    userSeed = input("Please enter a seed: ")
    # Implements the seed the user enters
    if userSeed != "":
        seedRand(userSeed)

    # Start of while loop
    while goAgain.lower() == "y":
        temporaryDiceList = []
        index = 0
        print("")
        print("You have $" + str(money))

        userBet = int(input("Enter a bet amount: $"))
        # To safeguard against bad user bets
        while userBet <= 0 or userBet > money:
            print("Please enter a number from 1 to " + str(money))
            userBet = int(input("Enter a bet amount: $"))

        userGuess = int(input("What number do you want to bet on (1-6)? "))
        # To safeguard against bad user guesses
        while userGuess < 1 or userGuess > 6:
            print("Invalid number, must be 1 to 6.")
            userGuess = int(input("What number do you want to bet on (1-6)? "))

        # Reiterates the user's choices
        print("You bet $" + str(userBet) + " on " + str(userGuess))
        diceRolls = roll()
        while index < 3:
            temporaryDiceList.append(str(diceRolls[index]))
            index += 1
        print("You rolled a")
        # Result of the dice rolls, in string form
        print("\t  " + ", ".join(temporaryDiceList))

        # Calculation portion of the code
        userWinnings = computeBetResult(diceRolls, userBet, userGuess)
        if userWinnings > 0:
            money = money + userWinnings
            print("You win!")
            print("You now have $" + str(money))
        else:
            money = money + userWinnings
            # Instructions for when money runs out
            # If money = 0, it will jump from the "You ended the game with $0" to the loop break
            if money == 0:
                print("You lose!")
                print("")
                print("You ended the game with $0")
            # The following else statement is the message the user gets when they get 0 matches
            # AKA their winnings are negative
            else:
                print("You lose!")
                print("You now have $" + str(money))

        if money > 0:
            goAgain = input("Would you like to go again? ")
        else:
            # Breaks the loop
            goAgain = ""

    # Outside of loop
    else:
        print("")
        print("You ended the game with $" + str(money))

# Calls the program
if __name__ == '__main__':
    main()
