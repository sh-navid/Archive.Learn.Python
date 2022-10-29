import numpy as np


L = []
for i in range(0, 16):
    L.append(i)


N = np.array(L)
print(N)


N = N.reshape(4, -1)
print(N)


N[:, -1] = [100, 200, 300, 400]
print(N)


N[-1] = [100, 200, 300, 400]
print(N)
