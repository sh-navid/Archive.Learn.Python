xo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def show():
    print("┌───┬───┬───┐")
    print("│ " + xo[0] + " │ " + xo[1] + " │ " + xo[2]+" │")
    print("├───┼───┼───┤")
    print("│ " + xo[3] + " │ " + xo[4] + " │ " + xo[5]+" │")
    print("├───┼───┼───┤")
    print("│ " + xo[6] + " │ " + xo[7] + " │ " + xo[8]+" │")
    print("└───┴───┴───┘")

def end():
    show()
    print("Game is ended")
    quit()

def check_end_of_game():
    if (xo[0]==xo[1]==xo[2]) or (xo[4]==xo[5]==xo[6]) or (xo[7]==xo[8]==xo[9]):
        end()
    elif (xo[0]==xo[3]==xo[6]) or (xo[1]==xo[4]==xo[7]) or (xo[2]==xo[5]==xo[8]):
        end()
    elif (xo[0]==xo[4]==xo[8]) or (xo[2]==xo[4]==xo[6]) :
        end()

player2 = "o"
player1 = "x"
while True:
    show()
    answer = int(input(f"Player({player1}) should play: "))
    if answer < 1 or answer > 9:
        continue

    answer -= 1
    if xo[answer] in ["x", "o"]:
        continue

    xo[answer] = player1
    player1, player2 = player2, player1

    check_end_of_game()


"""
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
Player(x) should play: 3
┌───┬───┬───┐
│ 1 │ 2 │ x │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
Player(o) should play: 6
┌───┬───┬───┐
│ 1 │ 2 │ x │
├───┼───┼───┤
│ 4 │ 5 │ o │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┴───┴───┘
"""