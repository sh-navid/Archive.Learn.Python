import numpy as np

L = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 4, 7],
    [1, 2, 3, 4, 8],
]

N = np.array(L)

F = N[N >= 4]

print(F)
