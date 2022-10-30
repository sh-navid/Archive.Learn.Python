import numpy as np

L = [
    [6, 2, 5, 1, 5],
    [6, 2, 6, 1, 6],
    [6, 2, 7, 1, 7],
    [6, 2, 8, 1, 8],
]
N = np.array(L)

print(np.max(N))
print(np.min(N))