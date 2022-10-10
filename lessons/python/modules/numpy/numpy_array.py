import numpy as np


my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_array, type(my_array), my_array.dtype, "Dimensions", my_array.ndim)
# [1 2 3 4 5 6 7 8 9] <class 'numpy.ndarray'> int64 Dimensions 1


print(my_array.shape)
# (9,)


# Slice 1D
print(my_array[1:3], "\n\n")
# [2 3]


my_array = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 20, 30, 40, 50, 60, 70, 80, 90]])
print(my_array, type(my_array), my_array.dtype, "Dimensions", my_array.ndim)
# [[ 1  2  3  4  5  6  7  8  9]
#  [10 20 30 40 50 60 70 80 90]] <class 'numpy.ndarray'> int64 Dimensions 2


print(my_array.shape)
# (2, 9)


# Slice 2D
print(my_array[1, 1:3])  # or
print(my_array[1][1:3], "\n\n")
# [20 30]
# [20 30]


# Access
my_array[0][0] = 100
print(my_array, type(my_array), my_array.dtype, "Dimensions", my_array.ndim)
# [[100   2   3   4   5   6   7   8   9]
#  [ 10  20  30  40  50  60  70  80  90]] <class 'numpy.ndarray'> int64 Dimensions 2
