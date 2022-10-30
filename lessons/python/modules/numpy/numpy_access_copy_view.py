import numpy as np

L = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 4, 7],
    [1, 2, 3, 4, 8],
]

N = np.array(L)

C = N.copy()
V = N.view()

V[0, 0] = 100
print(N)

C[0, 0] = -1
print(N)
print(C)


print(N.base)
# None

print(V.base)
'''
[[100   2   3   4   5]
 [  1   2   3   4   6]
 [  1   2   3   4   7]
 [  1   2   3   4   8]]
'''

print(C.base)
# None
