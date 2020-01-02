names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names)
names[0] = "Jon"
print(names[0])
print(names[-1])
print(names[2:])
# From index 2 to 3 (element at index 4 is not included)
print(names[2:4])
# This returns a copy of the list
print(names[:])

numbers = [16, 13, 11, 18, 20, 5]
greatest = numbers[0]
for number in numbers:
    if number > greatest:
        greatest = number
print(greatest)
