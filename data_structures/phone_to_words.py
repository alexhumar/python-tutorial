digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone_number = input("Phone: ")
words = ""
for digit in phone_number:
    words += digits.get(digit, "!") + " "
print(words)
