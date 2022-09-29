# Problem 2: Creating a math calculator
# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter calcution: ').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# If + then we need to produce output based on addition
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("beware! This calculator only operates + - / or *")