# Tuples are immutable. We can not add, change or remove elements
numbers = (1, 2, 3)
print(numbers[0])
# This will throw the error: 'tuple' object does not support item assignment.
# numbers[0] = 99

# Tuples are useful when you have a list of elements and you want to nobody can change that collection.
# But in the majority of scenarios we use lists
