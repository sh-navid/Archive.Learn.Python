import random


class Dice:
    name = "General Dice"
    min: int
    max: int
    step: int
    value = None

    def __init__(self, min=1, max=6, step=1) -> None:
        self.min = min
        self.max = max
        self.step = step

    def roll(self):
        self.value = random.randrange(self.min, self.max + 1, step=self.step)

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self) -> str:
        return str(self.get_name()) + ":" + str(self.value)

    def __repr__(self) -> str:
        return self.__str__()


class EvenDice(Dice):
    def __init__(self, min=2, max=6, step=2) -> None:
        super().__init__(min, max, step)
        self.name = "Even Dice"

    def get_name(self):
        return super().get_name() + "(Not Original)"


class OddDice(Dice):
    def __init__(self, min=1, max=6, step=2) -> None:
        super().__init__(min, max, step)
        self.name = "Odd Dice"

    def get_name(self):
        return super().get_name() + "(Not Original)"


my_dices = []

my_dices.append(Dice())
my_dices.append(Dice())
my_dices.append(Dice())

my_dices.append(EvenDice())
my_dices.append(EvenDice())
my_dices.append(EvenDice())

my_dices.append(OddDice())
my_dices.append(OddDice())
my_dices.append(OddDice())

for dice in my_dices:
    dice.roll()

print(my_dices)
