message = input("> ")
# split returns a list
words = message.split(" ")
print(words)
# I don't have emojis in linux, so I will map to another emoji
emojis = {
    ":)": ":D",
    ":(": ":/"
}
result = ""
for word in words:
    # If the key doesn't exists in the dictionary, the method will return the default value, which is the word
    result += emojis.get(word, word) + " "
print(result)
