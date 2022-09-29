# A program that rates how important a Birthday is

# We'll provide different output based on age
# 1-18 -> Important
# 21, 50, >65 -> Important
# All others -> Not important

# Receive age and store in age
age = eval(input("Enter age: "))

# and : if both true it returns true
# or : if either condition is true then true
# not : convert a true condition into a false

# if age is both greater than or equal to 1 and less than or equal to 1 and less than or equal to 18 its important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50 its important
if (age == 21) or (age == 50):
    print("Important Birthday")

# We check if age is less than 65, then convert True to False and vice versa
elif not(age < 65):
    print("Important Birthday")

# Else not important
else:
    print("sorry, not important birthday")
