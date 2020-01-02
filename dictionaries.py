# Stores information as key-value pairs
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
# This throws a KeyError because the key birth_date doesn't exists
# print(customer["birth_date"])
# We can use the method get to try getting a value. If the key doesn't exists, it will return None
print(customer.get("birth_date"))
print(customer.get("name"))
# We can add a default value:
print(customer.get("birth_date", "Jan 1 1980"))
# Editing the value of the key name
customer["name"] = "Jack Smith"
print(customer["name"])
# Adding a new key
customer["birth_date"] = "Jan 2 1995"
print(customer["birth_date"])
