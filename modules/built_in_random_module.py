# In Python we have a lot of built-in modules that can be consulted in the following link:
# https://docs.python.org/3/py-modindex.html
# This code shows how to use a built-in module for random number generation
# When we import built-in modules, the python interpreter knows where to find it. That's why we don't have references
# in the project to those modules (in this case, random module)
# The packages and modules can be consulted from External Libraries -> Python3.8 -> python3.8.
import random

# Generates random numbers between 0 and 1
for i in range(5):
    print(f'{i}: {random.random()}')

# Generates random integer numbers between those passed as arguments
for i in range(5):
    print(f'{i}: {random.randint(15, 25)}')

# Randomly picks an item from the list and returns it
members = ['John', 'Bob', 'Mary', 'Josh']
leader = random.choice(members)
print(leader)
