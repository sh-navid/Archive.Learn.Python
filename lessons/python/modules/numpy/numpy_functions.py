import numpy as np

#------------------------------------------------------------------
# Reshape
my_array = np.array([1, 2, 3, 4, 5, 6])
print(my_array, my_array.shape)
# [1 2 3 4 5 6]     (6,)


my_array = my_array.reshape(2, 3)
print(my_array, my_array.shape)
# [[1 2 3]
#  [4 5 6]]         (2, 3)


my_array = my_array.reshape(6)
print(my_array, my_array.shape)
# [1 2 3 4 5 6]     (6,)


my_array = my_array.reshape(3, 2)
print(my_array, my_array.shape)
# [[1 2]
#  [3 4]
#  [5 6]]           (3, 2)


my_array = my_array.reshape(6)
print(my_array, my_array.shape)
# [1 2 3 4 5 6]     (6,)


my_array = my_array.reshape(2, 3, 1)
print(my_array, my_array.shape)
# [[[1]
#   [2]
#   [3]]
#
#  [[4]
#   [5]
#   [6]]]           (2, 3, 1)


my_array = my_array.reshape(6)
print(my_array, my_array.shape)
# [1 2 3 4 5 6]     (6,)


my_array = my_array.reshape(1,-1,2) # When you do not know the correct value for dimention you can pass -1
print(my_array, my_array.shape)
# [[[1 2]
#  [3 4]
#  [5 6]]] (1, 3, 2)


my_array = my_array.reshape(-1) # pass -1 to make a flat array
print(my_array, my_array.shape)
# [1 2 3 4 5 6]     (6,)


#------------------------------------------------------------------
# np.concatenate()

x=np.array([4,5,6])
y=np.array([7,8,9])
print(np.concatenate([x,y]))
# [4 5 6 7 8 9]

#------------------------------------------------------------------
# np.stack()

print(np.stack([x,y]))
# [[4 5 6]
#  [7 8 9]]

print(np.hstack([x,y]))
# [4 5 6 7 8 9]

print(np.vstack([x,y]))
# [[4 5 6]
#  [7 8 9]]

print(np.dstack([x,y]))
# [[[4 7]
#   [5 8]
#   [6 9]]]
