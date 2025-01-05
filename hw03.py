'''
Dario Sanai
CS 87A, Fall 2024
sanai_dario_dariush@student.smc.edu
Homework 3
'''

# Define variables
vowelList = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
userInput = " "
vowelCount = 0
upperCaseCount = 0
lowerCaseCount = 0
letterCount = 0
averageWordLength = 0
numberOfWords = -1
# The "enter" key used to exit the loop will be counted as a word, so we set it at -1 to counteract

while userInput:    # Core loop

    userInput = input("Sentence please: ")
    inputList = list(userInput)     # The list command individually separates the letters and spaces
    # print(inputList)

    for vowel in inputList:
        if vowel in vowelList:  # VowelList was defined at the very beginning of the program
            vowelCount += 1
    # print("Vowel count: " + str(vowelCount))

    for upperCase in inputList:
        if ord("A") <= ord(upperCase) <= ord("Z"):
            upperCaseCount += 1
    # print("Uppercase letter count: " + str(upperCaseCount))

    for lowerCase in inputList:
        if ord("a") <= ord(lowerCase) <= ord("z"):
            lowerCaseCount += 1
    # print("Lowercase letter count: " + str(lowerCaseCount))

    for letter in inputList:
        if (ord("A") <= ord(letter) <= ord("Z")) or (ord("a") <= ord(letter) <= ord("z")):
            letterCount += 1
    # print("Letter count: " + str(letterCount))
    # "Simplify chained expressions" = make Boolean comparisons easier to understand

    for words in userInput.split(" "):
        numberOfWords += 1
    # print(userInput.split(" "))
    # print("Number of words: " + str(numberOfWords))

    if numberOfWords == 0:
        averageWordLength = 0
    else:
        averageWordLength = ("{:.2f}".format(letterCount / numberOfWords))
        # Formatting the variable in this way limits it to two decimal places
        # print("Average word length: " + str(averageWordLength))

print("There were " + str(vowelCount) + " vowels.")
print("There were " + str(upperCaseCount) + " uppercase letters.")
print("There were " + str(lowerCaseCount) + " lowercase letters.")
print("On average, words were " + str(averageWordLength) + " letters long.")
