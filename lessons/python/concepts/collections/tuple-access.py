# [Tuple]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Access Item
my_tuple = ("A", "B", "C", "C", "C")
print("Access Item:", my_tuple[1], type(my_tuple))
"""
Access Item: B <class 'tuple'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tuple Constructor (tuple)
my_tuple = tuple(("A", "B", "C"))
print("Tuple:", my_tuple)
"""
Tuple: ('A', 'B', 'C')
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Loop, Iterate
my_tuple = ("A", "B", "C")
for i in my_tuple:
    print("Loop:", i)
"""
Loop: A
Loop: B
Loop: C
"""

for i in range(len(my_tuple)):
    print(f"Loop {i}:", my_tuple[i])
"""
Loop 0: A
Loop 1: B
Loop 2: C
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Delete Tuple Completely
my_tuple = ("A", "B", "C")
del my_tuple
# print(my_tuple)
"""
NameError: name 'my_tuple' is not defined
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy? Not working
my_tuple = ("A", "B", "C")
my_tuple2 = my_tuple
my_tuple3 = tuple(my_tuple)
print("Is my_tuple the same as my_tuple2?", my_tuple is my_tuple2)
print("Is my_tuple the same as my_tuple3?", my_tuple is my_tuple3)
"""
Is my_tuple the same as my_tuple2? True
Is my_tuple the same as my_tuple3? True
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Len
print("Length:", ("A", "B", "C").__len__())
print("Length:", len(("A", "B", "C")))
"""
Length: 3
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Count
print("Count:", ("A", "B", "C", "C", "c").count("C"))
"""
Count: 2
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Slice
my_tuple = ("A", "B", "C", "D", "E", "F", "G", "H")
print("my_tuple[-1]    ", my_tuple[-1])
print("my_tuple[1]     ", my_tuple[1])
print("my_tuple[1:]    ", my_tuple[1:])
print("my_tuple[:4]    ", my_tuple[:4])
print("my_tuple[1:4]   ", my_tuple[1:4])
print("my_tuple[-5:-3] ", my_tuple[-5:-3])
"""
my_tuple[-1]     H
my_tuple[1]      B
my_tuple[1:]     ('B', 'C', 'D', 'E', 'F', 'G', 'H')
my_tuple[:4]     ('A', 'B', 'C', 'D')
my_tuple[1:4]    ('B', 'C', 'D')
my_tuple[-5:-3]  ('D', 'E')
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Join
print("Join:", ("A", "B", "C") + ("A", "B", "C"))
"""
Join: ('A', 'B', 'C', 'A', 'B', 'C')
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unpack
my_tuple = ("A", "B", "C")
x, y, z = my_tuple
print("Unpack:", x, y, z)
"""
Unpack: A B C
"""

x, *y = my_tuple
print("Unpack:", x, y)
"""
Unpack: A ['B', 'C']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check (in)
my_tuple = ("A", "B", "C")
print("Is 'C' in my_tuple?", "C" in my_tuple)
print("Is 'K' in my_tuple?", "K" in my_tuple)
"""
Is 'C' in my_tuple? True
Is 'K' in my_tuple? False
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Index
my_tuple = ("A", "B", "C")
print("Index:", my_tuple.index("B"))
"""
Index: 1
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tuple with one item
my_tuple = ("A",)
print("Tuple with one item:", my_tuple, type(my_tuple))
"""
Tuple with one item: ('A',) <class 'tuple'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# [Not Available in Tuples]
# my_tuple[1] = "Y"
"""
TypeError: 'tuple' object does not support item assignment
"""
# my_tuple.append("D")
"""
AttributeError: 'tuple' object has no attribute 'append'
"""
# my_tuple.insert(1, "D")
"""
AttributeError: 'tuple' object has no attribute 'insert'
"""
# my_tuple.remove("B")
"""
AttributeError: 'tuple' object has no attribute 'remove'
"""
# del my_tuple[0]
"""
TypeError: 'tuple' object doesn't support item deletion
"""
# my_tuple.pop(1)
"""
AttributeError: 'tuple' object has no attribute 'pop'
"""
# my_tuple.copy()
"""
AttributeError: 'tuple' object has no attribute 'copy'
"""
# my_tuple.extend(["K", "F"])
"""
AttributeError: 'tuple' object has no attribute 'extend'
"""
# my_tuple.clear()
"""
AttributeError: 'tuple' object has no attribute 'clear'
"""
# my_tuple.reverse()
"""
AttributeError: 'tuple' object has no attribute 'reverse'
"""
# my_tuple.sort()
"""
AttributeError: 'tuple' object has no attribute 'sort'
"""