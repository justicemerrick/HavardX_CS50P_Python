# Allocate a grade for a student depending on age

# prompt user to enter age
age = eval(input("Enter age: "))

# if age is 5 go to kindergarten
if (age == 5):
     print("Go to kindergarten")

# Ages 6 through 17 goes to grades between 1 and 12
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))

# if age is greater than 17
elif not(age <= 17):
    print("youre old enough to be in college")

else:
    print("stay home and drink milk")