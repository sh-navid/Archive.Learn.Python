import random
from tkinter import *
from enum import Enum


BACK_COLOR = "#1e1e1e"
FORE_COLOR = "#fefefe"


class Choices(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


player_choices = [None, None]


def choose_one(btn, index):
    global player_choices
    my_choice = random.choice([Choices.ROCK, Choices.PAPER, Choices.SCISSORS])
    player_choices[index] = my_choice
    btn.config(text=my_choice.name)

    p1, p2 = player_choices
    if (
        (p1 is Choices.PAPER and p2 is Choices.ROCK)
        or (p1 is Choices.ROCK and p2 is Choices.SCISSORS)
        or (p1 is Choices.SCISSORS and p2 is Choices.PAPER)
    ):
        lbl_winner.config(text="Player 1 is the winner")
    elif p1 is p2:
        lbl_winner.config(text="Game is Draw")
    else:
        lbl_winner.config(text="Player 2 is the winner")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window = Tk()
window.geometry("350x350")
window.title("Rock, Paper, Scissors")
window.config(bg=BACK_COLOR)


frame = Frame(window)
frame.config(bg=BACK_COLOR)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)


lbl1 = Label(frame, text="PLAYER 1")
lbl1.config(background=BACK_COLOR)
lbl1.config(foreground=FORE_COLOR)
lbl1.pack()


btn_player1 = Button(frame)
btn_player1.config(text="Player 1")
btn_player1.config(background=BACK_COLOR)
btn_player1.config(foreground=FORE_COLOR)
btn_player1.config(command=lambda: choose_one(btn_player1, 0))
btn_player1.pack()


lbl1 = Label(frame, text="PLAYER 2")
lbl1.config(background=BACK_COLOR)
lbl1.config(foreground=FORE_COLOR)
lbl1.pack()


btn_player2 = Button(frame)
btn_player2.config(text="Player 2")
btn_player2.config(background=BACK_COLOR)
btn_player2.config(foreground=FORE_COLOR)
btn_player2.config(command=lambda: choose_one(btn_player2, 1))
btn_player2.pack()


lbl_winner = Label(window, text="No Winner Yet...")
lbl_winner.config(background=BACK_COLOR)
lbl_winner.config(foreground=FORE_COLOR)
lbl_winner.pack()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
window.mainloop()
