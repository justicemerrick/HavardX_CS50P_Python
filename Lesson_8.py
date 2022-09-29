#Ask user their name, and Remove whitespace from strings
name = input("what's your name: ").strip().title()

# split user's name into first name and last name
first, last = name.split(" ")

#say hello to user
print(f"Hello, {first}")