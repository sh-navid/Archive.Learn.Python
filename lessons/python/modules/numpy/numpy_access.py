import numpy as np

# ------------------------------------------------------------------
# View, Copy
my_array = np.array([1, 2, 3, 4, 5])
my_array_copy = my_array.copy()
my_array_view = my_array.view()


my_array_copy[0] = 100
print(my_array, my_array_copy, my_array_copy.base)
# [1 2 3 4 5] [100   2   3   4   5] None


my_array_view[0] = 100
print(my_array, my_array_view, my_array_view.base)
# [100   2   3   4   5] [100   2   3   4   5] [100   2   3   4   5]


# ------------------------------------------------------------------
# Iterate


my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
my_array = my_array.reshape(2, 3, -1)


for x in my_array:
    for y in x:
        for z in y:
            print(z)
"""
1
2
3
4
5
6
7
8
9
10
11
12
"""


for item in np.nditer(my_array):
    print(item)
"""
1
2
3
4
5
6
7
8
9
10
11
12
"""

for index, item in np.ndenumerate(my_array):
    print(index, item)
"""
(0, 0, 0) 1
(0, 0, 1) 2
(0, 1, 0) 3
(0, 1, 1) 4
(0, 2, 0) 5
(0, 2, 1) 6
(1, 0, 0) 7
(1, 0, 1) 8
(1, 1, 0) 9
(1, 1, 1) 10
(1, 2, 0) 11
(1, 2, 1) 12
"""
