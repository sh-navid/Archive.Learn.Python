import numpy as np

L = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 4, 7],
    [1, 2, 3, 4, 8],
]

N = np.array(L)

print(N[:3, :3])
print(N[1:, 2:])
