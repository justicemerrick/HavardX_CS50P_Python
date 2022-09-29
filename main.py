# Problem: Receive miles and convert to kilometers
# 1. Ask the user to input miles and assign it to the miles variable
miles = input('Enter miles: ')

# 2. Convert from string to int
miles = int(miles)

# kilometers = miles * 1.60934
# 3. Perform calculations by multiplying 1.60934 times miles
Km = miles * 1.60934

# Print results using format
print("{} miles equals {} kilometers".format(miles, Km))

# Enter miles 5
# 5