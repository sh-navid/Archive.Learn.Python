from enum import Enum
import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Result(Enum):
    ROCK = 0
    PAPER = 2
    SCISSORS = 3
    NOT_DEFINED = 4


class Player:
    outcome = Result.NOT_DEFINED
    name = None

    def __init__(self, player_name) -> None:
        self.name = player_name

    def __str__(self) -> str:
        return self.name + " - " + self.outcome.name

    def play(self):
        self.outcome = random.choice([Result.ROCK, Result.PAPER, Result.SCISSORS])


def who_is_the_winner(p1: Player, p2: Player):
    if (
        (p1.outcome is Result.ROCK and p2.outcome is Result.SCISSORS)
        or (p1.outcome is Result.SCISSORS and p2.outcome is Result.PAPER)
        or (p1.outcome is Result.PAPER and p2.outcome is Result.ROCK)
    ):
        return p1
    return p2


player1 = Player("PLAYER ONE")
player2 = Player("PLAYER TWO")

player1.play()
player2.play()

print(player1)
print(player2)

print("Winner:", who_is_the_winner(player1, player2))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# اگر هر دو بازیکن مقدار مساوی بیاورند، بازیکن دوم برنده اعلام میشود
# برنامه را به شکلی تغییر دهید که بتواند حالت مساوی شدن را هم شامل
# شود
