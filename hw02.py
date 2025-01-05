'''
Dario Sanai
CS 87A, Fall 2024
sanai_dario_dariush@student.smc.edu
Homework 2
'''


userInput = input("Whose BMI shall I calculate: ")
# I stored their input as a variable because it is needed for three lines of the code
print("Okay, first I need " + userInput.title() + "'s height...")
# Perfect example
feetValue = int(input("First feet: "))
inchesValue = int(input("Next inches: "))

weightValue = float(input("Now I need " + userInput.title() + "'s weight in pounds:"))

overallHeightInches = int((feetValue * 12) + inchesValue)
# print(overallHeightInches). Used this to test it out when initially creating the variable.

overallHeightMeters = float(overallHeightInches / 39.3701)
# print(overallHeightMeters). Same reasoning as the above comment.

overallMassKilograms = float(weightValue / 2.20462)
# print(overallMassKilograms). Ditto.

overallBMI = float(overallMassKilograms / (overallHeightMeters * overallHeightMeters))
print(userInput.title() + "'s BMI is " + str(overallBMI))
# The final product. I compared it with the government's official BMI calculator and it matched up perfectly.

