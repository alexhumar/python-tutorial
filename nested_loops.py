my_list = []
for x in range(4):
    # Inner loop
    for y in range(3):
        my_list.append((x, y))
print(my_list)

numbers = [5, 2, 5, 2, 2]
for number in numbers:
    line = ""
    for x in range(number):
        line += "x"
    print(line)
