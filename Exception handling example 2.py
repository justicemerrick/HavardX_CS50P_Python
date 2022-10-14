class DogNameError(Exception):

    def __int__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

try:
    dogName = input("What is your dogs name: ")

    if any(char.isdigit() for char in dogName):

        raise DogNameError

except DogNameError:
    print("Your dog's name cant contain a number")
    # this is how custom exceptions are made