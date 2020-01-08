for item in "Python":
    print(item)

my_list = ["Banana", "Apple", "Strawberry"]
for item in my_list:
    print(item)

# range function can receive the start number, the final number (not included), and the increment number
for number in range(5, 10, 2):
    print(number)

prices = [10.4, 20, 44.67, 33.2]
total_price = 0
for price in prices:
    total_price += price
print(f"Total: ${total_price}")
