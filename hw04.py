'''
Dario Sanai
CS87A, Fall 2024
sanai_dario_dariush@student.smc.edu
Homework 4
'''

import soundLib

# Create Morse Code Dictionary: use letters as keys and Morse representations as values.
morseCodeDictionary = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
"I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
"R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--.."}
# Initialize variables
printStatementList = []
audioInput = " "
userInput = " "
message = " "

while userInput:
    printStatement = ""
    userInput = input("Input a message to translate into Morse Code: ")
    # Analyze each character of user's input; ignore input that isn't a letter or a space
    for letter in userInput.upper():
        # Put a space in between each letter and three spaces in between each word
        if letter in morseCodeDictionary:
            printStatement += morseCodeDictionary[letter] + " "
        elif letter == " ":
            printStatement += "  "
    # Convert it into a list to remove the end space
    printStatementList = printStatement.split(" ")
    del printStatementList[-1]
    printStatement = " ".join(printStatementList)
    # Convert it back into a list
    if userInput != "":
        print("Your message translated to Morse Code is:")
        print(printStatement)
        audioInput = input("Would you like to hear the message? ")
        if audioInput == "y":
        # Call the first part of the sound function
            soundLib.initSound()
            for morseCharacter in printStatement:
                if morseCharacter == ".":
                    soundLib.addMorseDot()
                elif morseCharacter == "-":
                    soundLib.addMorseDash()
                elif morseCharacter == " ":
                    soundLib.addMorsePause()
            # Call the last part of the sound function
            soundLib.playSound()
    else:
        print("Goodbye!")