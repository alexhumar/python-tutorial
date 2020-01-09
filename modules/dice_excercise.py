import random


class Dice:
    @staticmethod
    def roll_attempt():
        return random.randint(1, 6)

    def roll(self):
        first_attempt = self.roll_attempt()
        second_attempt = self.roll_attempt()
        # When we return a tuple from a function, we don't have to write parenthesis
        return first_attempt, second_attempt


dice = Dice()
print(dice.roll())
