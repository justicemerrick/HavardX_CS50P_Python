# this program will print even if an exception is triggered or not.

num1, num2 = input("Enter 2 values to divide: ").split()

try:
    quotient = int(num1) / int(num2)

    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You cannot divide by zero")

else:
    print("you didn't raise an exception")

finally:
    print("I execute no matter what")
