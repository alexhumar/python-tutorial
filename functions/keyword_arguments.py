def greet_user(first_name: str, last_name: str):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard!")


def calculate_cost(total: float, shipping: float, discount: float):
    print(f"Calculating cost... {total} | {shipping} | {discount}")


# first_name and last_name are positional parameters
greet_user("John", "Smith")

# Keyboard parameters are those whose position doesn't matter
greet_user(last_name="Smith", first_name="John")
# Helps in some cases to make the code more readable. For example:
calculate_cost(50, 5, 0.1)
# Its equivalent to
calculate_cost(total=50, shipping=5, discount=0.1)
# KEYWORD ARGUMENTS MUST COME AFTER POSITIONAL ARGUMENTS
greet_user("John", last_name="Smith")
