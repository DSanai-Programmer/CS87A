'''
Dario Sanai
CS87A, Fall 2024
sanaidario@gmail.com
Project 1
'''

# I am going to separate the code by parts to keep everything organized and easy to understand

# Part 1:

# Declare variables
# I convert the input to "float" since it automatically comes out as a string
purchasePrice = float(input("Enter the vehicle's purchase price: "))
cashDownPayment = float(input("Enter your down payment for the vehicle: "))
salesTax = float(input("Enter the sales tax on the transaction (for 8.25% enter 8.25): "))

tradeInAnswer = input("Do you have a vehicle to trade in? (y/n): ")
tradeIn = 0
amountOwedOnTrade = 0
if tradeInAnswer.lower() == "y":
    tradeIn = float(input("Enter the trade-in value for your current vehicle: "))
    amountOwedOnTrade = float(input("Enter the amount owed on your current vehicle: "))

# If the user inputs "n", the conditional is skipped. The tradeIn and amountOwedOnTrade variables stay at 0
# All the inputs the user put earlier are used in these equations
totalDownPayment = float(cashDownPayment + (tradeIn - amountOwedOnTrade))
loanAmount = float((purchasePrice - totalDownPayment) * (1 + salesTax/100))

print("Your overall down payment is $" + str(totalDownPayment))
print("Your overall loan amount is $" + str(loanAmount))

# I must convert the variables to strings because I cannot combine strings and floats

# Part 2:

print("Enter the length of your loan...")
print("\t1: 3 years")
print("\t2: 4 years")
print("\t3: 5 years")
print("\t4: 6 years")

numberOfPayments = 0

# PyCharm puts a warning if I don't define numberOfPayments beforehand, although it isn't necessary

loanLengthChoice = int(input("Select an option: "))
# Initial mistake: I did not set the variable to an int, which made GradeScope go to the "else" option by default
if loanLengthChoice == 1:
    print("You selected a 3 year loan with a total of 36 monthly payments.")
    numberOfPayments = 36
elif loanLengthChoice == 2:
    print("You selected a 4 year loan with a total of 48 monthly payments.")
    numberOfPayments = 48
elif loanLengthChoice == 3:
    print("You selected a 5 year loan with a total of 60 monthly payments.")
    numberOfPayments = 60
elif loanLengthChoice == 4:
    print("You selected a 6 year loan with a total of 72 monthly payments.")
    numberOfPayments = 72
else:
    print("You selected a 5 year loan with a total of 60 monthly payments.")
    numberOfPayments = 60

# print(numberOfPayments)

# Part 3:

percentDown = (totalDownPayment / purchasePrice * 100)
# print(percentDown)
interestRate = 0
# Again, PyCharm complains if I don't define the variable before the conditionals

if loanLengthChoice == 1:
# Make sure to convert the percentDown into a string, since you are combining it with two other sets of strings
    if percentDown < 20:
        print("With " + str(percentDown) + "% down and a 3 year loan we can offer you an interest rate of 6.25%")
        interestRate = 6.25
    elif percentDown >= 20:
        print("With " + str(percentDown) + "% down and a 3 year loan we can offer you an interest rate of 5.3%")
        interestRate = 5.3
elif loanLengthChoice == 2:
    if percentDown < 20:
        print("With " + str(percentDown) + "% down and a 4 year loan we can offer you an interest rate of 6.75%")
        interestRate = 6.75
    elif percentDown >= 20:
        print("With " + str(percentDown) + "% down and a 4 year loan we can offer you an interest rate of 5.7%")
        interestRate = 5.7
elif loanLengthChoice == 3:
    if percentDown < 20:
        print("With " + str(percentDown) + "% down and a 5 year loan we can offer you an interest rate of 7.25%")
        interestRate = 7.25
    elif percentDown >= 20:
        print("With " + str(percentDown) + "% down and a 5 year loan we can offer you an interest rate of 6.1%")
        interestRate = 6.1
elif loanLengthChoice == 4:
    if percentDown < 20:
        print("With " + str(percentDown) + "% down and a 6 year loan we can offer you an interest rate of 7.5%")
        interestRate = 7.5
    elif percentDown >= 20:
        print("With " + str(percentDown) + "% down and a 6 year loan we can offer you an interest rate of 6.8%")
        interestRate = 6.8
else:
    if percentDown < 20:
        print("With " + str(percentDown) + "% down and a 5 year loan we can offer you an interest rate of 7.25%")
        interestRate = 7.25
    elif percentDown >= 20:
        print("With " + str(percentDown) + "% down and a 5 year loan we can offer you an interest rate of 6.1%")
        interestRate = 6.1

# print(interestRate)

# Part 4:

monthlyInterest = (interestRate / 1200)
# print(monthlyInterest)
denominatorMonthlyPayment = 1 - (1 + monthlyInterest)**-numberOfPayments
# print(denominatorMonthlyPayment)
monthlyPayment = loanAmount * (monthlyInterest / denominatorMonthlyPayment)
# print(monthlyPayment)

print("Your estimated monthly payment is $" + str(monthlyPayment) + " a month")

# The output I get for the monthlyPayment has a different last digit than those in run 1 and 2. I am unsure why.
