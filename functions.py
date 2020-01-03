def greet_user(name: str):
    print(f"Hi {name}!")
    print("Welcome aboard!")


def say_bye(first_name: str, last_name: str):
    print(f"Good bye, {first_name} {last_name}!")
    print("Have a nice day!")


print("Start")
greet_user("John")
greet_user("Mary")
say_bye("Steve", "Smith")
print("Finish")

# I've added a type for each parameter that I've declared
# Parameters vs. Arguments:
# Parameters: are the placeholders that we define in a function for receiving information (e.g: name)
# Arguments: are the actual piece of information that we supply to a function (e.g.: "John", "Mary")
