# Notes
# while loops can have else statements
#   while(x):
#   else:
# else will execute when x, the conditional for the while loop, is finally false
# in most language, for and while loops have the same functions but in Python, for loops are only used to iterate through ranges
# break statements exits the loop completely
# continue statements exits one iteration of the loop

balance = 2250
interestRate = 0.045
term = 120

# also could have done a while loop
for i in range(term):
    print("Month ", i+1, "          ", "Interest: $ ", (balance * interestRate) / 12, "         Balance: $ ", (balance + ((balance * interestRate) / 12)), sep = "")
    balance = (balance + ((balance * interestRate) / 12))