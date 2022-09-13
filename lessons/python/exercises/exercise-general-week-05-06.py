from enum import Enum

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class RiskLevel(Enum):
    WILD = 1
    SAFE = 2
    RISKY = 3


class Animal:
    name: str = None
    risk = RiskLevel.RISKY

    def __init__(self, name: str, risk_level=RiskLevel.RISKY) -> None:
        self.name = name
        self.risk = risk_level

    def __str__(self) -> str:
        return "{}:({}>{}>{})".format(
            self.name, self.__class__.__name__, self.risk.name, self.movement()
        )

    def __repr__(self) -> str:
        return self.__str__()

    def movement(self):
        pass


class Mamal(Animal):
    def movement(self):
        return "Walk"


class Bird(Animal):
    def movement(self):
        return "Fly"


class Fish(Animal):
    def movement(self):
        return "Swim"


my_animals = []


my_animals.append(Mamal("Lion", RiskLevel.WILD))
my_animals.append(Bird("BlueJay", RiskLevel.SAFE))
my_animals.append(Bird("Hen"))
my_animals.append(Bird("Rooster"))
my_animals.append(Fish("Dolphin", RiskLevel.SAFE))


print(my_animals)

# EXERCISE:
# Save to file
