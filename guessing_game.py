secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    number = float(input("Guess: "))
    guess_count += 1
    if number == secret_number:
        print("You won!")
        # break ends the while loop
        break
# This is the else of THE WHILE loop! It executes if the while loop completes successfully with no breaks.
# In this case, the while condition will be false. It's similar to an if statement in that way.
else:
    print("You loose!")
