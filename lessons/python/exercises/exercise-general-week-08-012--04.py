import numpy as np

D = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
])


L = [8, 8, 8, 8, 8, 8, 8, 8, 8]


X = {
    0: '-',
    1: '@',
    2: '#',
}

p1, p2 = 1, 2


def show():
    for row in D:
        for cell in row:
            print(X[cell], end="")
            # print(cell, end="")
        print()


def check_4(row):
    if (np.sum(row) == 4):
        print("@ is the winner")
        exit()
    if (np.sum(row) == 8):
        print("# is the winner")
        exit()


def check_4_square(M):
    for x in [0, 1, 2, 3]:
        check_4(M[x])
        check_4(M[:, x])
    check_4(np.array([M[0, 0], M[1, 1], M[2, 2], M[3, 3]]))
    check_4(np.array([M[0, 3], M[1, 2], M[2, 1], M[3, 0]]))


def check_winner():
    for row in range(0, 6):
        for col in range(0, 6):
            #  Div and Conq
            M = D[row:row+4, col:col+4]
            # print(M)
            check_4_square(M)


show()
while True:
    i = int(input(f"Enter 1-9: "))
    if i >= 1 and i <= 9:
        D[L[i-1]][i-1] = p1
        L[i-1] -= 1
        p1, p2 = p2, p1
        show()
        check_winner()
