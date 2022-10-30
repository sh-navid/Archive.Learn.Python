import numpy as np

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
