coordinates = (1, 2, 3)
# We could do this
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

t = x * y * z
# But it's too repetitive

# We can do this, with the same effect
# Here we are unpacking the tuple into three variables
x, y, z = coordinates
print(x)
print(y)
print(z)

# We also can unpack a list in a similar way...
