# [Identiry Operators]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Each object in memory has a unique ID

x = 100
y = 200
print(f"x={x}, y={y}, id(x)={id(x)}, id(y)={id(y)}, x is y ? {x is y}")
x = y
print(f"x={x}, y={y}, id(x)={id(x)}, id(y)={id(y)}, x is y ? {x is y}")
y = 160
print(f"x={x}, y={y}, id(x)={id(x)}, id(y)={id(y)}, x is y ? {x is y}")
"""
x=100, y=200, id(x)=2252089789776, id(y)=2252089792976, x is y ? False
x=200, y=200, id(x)=2252089792976, id(y)=2252089792976, x is y ? True
x=200, y=160, id(x)=2252089792976, id(y)=2252089791696, x is y ? False
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = True
print(x is True)  # True

y = False
print(y is True)  # False
print(y is not True)  # True

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = [1, 2, 3]
y = [1, 2, 3]
k = [1, 2]
t = [2, 3, 1]
r = x  # same object
c = x.copy()
d = list(x)

print("x == y", x == y)  # same content but not same object
print("x == k", x == k)
print("x == t", x == t)

print("x is y", x is y)  # same content but not same object
print("x is k", x is k)
print("x is t", x is t)
print("x is r", x is r)  # same content, same object
print("x is c", x is c)  # same content but not same object
print("x is d", x is d)

"""
x == y True
x == k False
x == t False
x is y False
x is k False
x is t False
x is r True
x is c False
x is d False
"""

print(f"{id(r)}, {id(x)}")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(None is None)  # True
print(str is str)  # True
print(int is str)  # False
print(1 is 1)  # True
print(id(1), id(1), id(1))  # 2497011253488 2497011253488 2497011253488 :) Amazing
