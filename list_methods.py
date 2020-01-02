numbers = [1, 4, 5, 9, 5, 10]
print(numbers)
numbers.append(22)
print(numbers)
# Takes the index in which the value will be inserted
numbers.insert(0, 30)
print(numbers)
numbers.remove(4)
print(numbers)
# Removes the element at the given index. If no index was given, removes the last element
numbers.pop()
print(numbers)
# Throws an error if the element is not in the list
print(numbers.index(1))
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers)
# And backwards
numbers.reverse()
print(numbers)
copy_numbers = numbers.copy()
numbers.clear()
print(numbers)
print(copy_numbers)

# Removing duplicates - my solution
duplicated_list = [1, 7, 8, 4, 7, 1, 6]
for item in duplicated_list:
    if duplicated_list.count(item) > 1:
        duplicated_list.remove(item)
print(duplicated_list)

# Mosh's solution
duplicated_list = [1, 7, 8, 4, 7, 1, 6]
unique = []
for item in duplicated_list:
    if item not in unique:
        unique.append(item)
print(unique)