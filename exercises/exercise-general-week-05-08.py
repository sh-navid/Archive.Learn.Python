import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Dice:
    number = None

    def roll(self):
        self.number = random.choice([1, 2, 3, 4, 5, 6])

    def __str__(self):
        return str(self.number)


dice1 = Dice()
dice2 = Dice()

dice1.roll()
dice2.roll()

print(dice1, dice2)
