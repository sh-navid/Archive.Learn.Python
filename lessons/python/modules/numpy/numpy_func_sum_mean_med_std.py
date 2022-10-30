import numpy as np

L = [
    [6, 2, -5, 1, 5],
    [6, 2, -6, 1, 6],
    [6, 2, -7, 1, 7],
    [6, 2, -8, 1, 8],
]
N = np.array(L)

print(np.mean(N))
print(np.median(N))
print(np.std(N))
print(np.sum(N))
print(np.abs(N))