# Dario Sanai
# sanai_dario_dariush@student.smc.edu
# CS87A, Fall 2024
# Homework 1 -- MadLibs!

print("Welcome to MadLibs 1.0")

# Create variables
userName = ""           # Stores the user's name
userAnimal = ""         # Stores the user's chosen animal
userNumber = 0          # Stores the user's favorite number
numFootPrints = ""      # Stores the number of footprints left

# Get user input
userName = input("Gimme your name: ").title()
userAnimal = input("What's a 4 legged animal (in plural form): ")
userNumber = int(input("What's your favorite number: "))

# Check variable values
# print(userName)
# print(userAnimal)
# print(userNumber)

# Do math
numFootPrints = 2 + 4 * userNumber
# print(numFootPrints)

# Display MadLib
print(userName + " and " + str(userNumber) + " \"" + userAnimal + "\" walked along...")
print("They left " + str(numFootPrints) + " footprints in the sand!")



