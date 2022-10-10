import numpy as np


my_array = np.array([2.8, 3.6, 4.1])
print(my_array, my_array.dtype)
# [2.8 3.6 4.1] float64


my_array = my_array.astype("i1")
print(my_array, my_array.dtype)
# [2 3 4] int8


my_array = my_array.astype("S1")
print(my_array, my_array.dtype)
# [b'2' b'3' b'4'] |S1
