from enum import Enum
import random


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


def winner(p1: Player, p2: Player):
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Answer 1,2 <-----
    if p1.outcome == p2.outcome:
        print(f"({p1},\t{p2})\t=> Draw between ({p1.name}, {p2.name})")
        return p1
    elif (
        (p1.outcome is Result.ROCK and p2.outcome is Result.SCISSORS)
        or (p1.outcome is Result.SCISSORS and p2.outcome is Result.PAPER)
        or (p1.outcome is Result.PAPER and p2.outcome is Result.ROCK)
    ):
        print(f"({p1},\t{p2})\t=> {p1.name} is stronger")
        return p1
    else:
        print(f"({p1},\t{p2})\t=> {p2.name} is stronger")
        return p2


player1 = Player("PLAYER 1")
player2 = Player("PLAYER 2")
player3 = Player("PLAYER 3")

player1.play()
player2.play()
player3.play()

print(player1)
print(player2)
print(player3)
print("------------")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2 <-----
if player1.outcome == player2.outcome == player3.outcome:
    print("Draw between 3 players")
elif (
    player1.outcome != player2.outcome
    and player2.outcome != player3.outcome
    and player1.outcome != player3.outcome
):
    print("Everyone can attack the other one!")
else:
    winner(winner(player1, player2), player3)
