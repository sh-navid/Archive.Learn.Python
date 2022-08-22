# [Set]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# <> Angle brackets,    Chevron
# {} Braces
# () Parentheses
# [] brackets
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Access
my_set = set([1, 2, 3, 3, 3])
print("Using set() constructor:", my_set, type(my_set))
"""
Using set() constructor: {1, 2, 3} <class 'set'>
"""

my_set = {1, 4, 6, 6, 6, 6, 8, 10}
print("my_set:", my_set, type(my_set))
"""
my_set: {1, 4, 6, 8, 10} <class 'set'>
"""

for x in my_set:
    print("Access:", x)
"""
Access: 1
Access: 4
Access: 6
Access: 8
Access: 10
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Length
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
print("Length:", len(my_set))
"""
Length: 5
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check (in)
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
print("Check:", 3 in my_set)
print("Check:", 6 not in my_set)
print("Check:", 4 in my_set)
"""
Check: False
Check: False
Check: True
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Add
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
# my_set[3]=12
"""
TypeError: 'set' object does not support item assignment
"""
my_set.add(12)
print("Add:", my_set)
"""
Add: {1, 4, 6, 8, 10, 12}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Update
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
my_set.update({100})
my_set.update((14, 15))
my_set.update(["A"])
print("Update:", my_set)
"""
Update: {1, 4, 6, 8, 10, 14, 15, 100, 'A'}
"""
my_set = my_set.union("U")
print("Union:", my_set)
"""
Union: {1, 4, 100, 6, 8, 10, 'A', 14, 15, 'U'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove, Discard, Pop
# Remove raise error if not exists
# Discard do not raise error if not exists
# Remove the last item
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
# my_set.remove(100)
"""
KeyError: 100
"""
my_set.remove(4)
my_set.discard(1)
my_set.discard(100)
print("Remove, Discard:", my_set)
"""
Remove, Discard: {6, 8, 10}
"""
print("Pop:", my_set.pop(), my_set)
"""
Pop: 6 {8, 10}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Del
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
del my_set
# print(my_set)
"""
NameError: name 'my_set' is not defined
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
my_set2 = my_set
my_set3 = set(my_set)
my_set4 = my_set.copy()
print("Is my set same as my_set2?", my_set2 is my_set)
print("Is my set same as my_set3?", my_set3 is my_set)
print("Is my set same as my_set4?", my_set4 is my_set)
"""
Is my set same as my_set2? True
Is my set same as my_set3? False
Is my set same as my_set4? False
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Clear
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
my_set.clear()
print("Clear:", my_set)
"""
Clear: set()
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Union
my_set = {1, 4, 6, 6, 6, 6, 8, 10}
my_set = my_set.union(["A", "A", "A", "B"])
print("Union:", my_set)
"""
Union: {1, 4, 'A', 6, 8, 10, 'B'}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Intersection
my_set = {1, 3, 5, 7, 10}
my_set2 = {2, 4, 6, 8, 10}
print("Intersection:", my_set.intersection(my_set2))
"""
Intersection: {10}
"""
# Intersection Update in Place
my_set = {1, 3, 5, 7, 10}
my_set2 = {2, 4, 6, 8, 10}
my_set.intersection_update(my_set2)
print("Intersection Update:", my_set)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Difference
my_set = {1, 3, 5, 7, 10}
my_set2 = {2, 4, 6, 8, 10}
print(
    "Difference:", my_set.difference(my_set2)
)  # use my_set.difference_update() for inplace update
"""
Difference: {1, 3, 5, 7}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Symmetric Difference
my_set = {1, 3, 5, 7, 10}
my_set2 = {2, 4, 6, 8, 10}
print(
    "Symmetric:", my_set.symmetric_difference(my_set2)
)  # use my_set.symmetric_difference_update() for inplace update
"""
Symmetric: {1, 2, 3, 4, 5, 6, 7, 8}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Disjoint, Subset, Superset
# Disjoint  -> True -> if -> no     items of x in y
# Subset    -> True -> if -> all    items of x in y
# Superset  -> True -> if -> all    items of y in x
x = {1, 3, 5, 7, 10}
y = {2, 4, 6, 8, 10}
print("Disjoint:", x.isdisjoint(y))
x.remove(10)
print("Disjoint:", x.isdisjoint(y))
"""
Disjoint: False
Disjoint: True
"""

x = {1, 2, 3, 4}
y = {1, 2, 3, 100}
print("Subset:", x.issubset(y))
x.remove(4)
print("Subset:", x.issubset(y))
"""
Subset: False
Subset: True
"""

x = {1, 2, 3, 4, 5, 6, 7}
y = {1, 2, 3, 100}
print("Superset:", x.issuperset(y))
y.remove(100)
print("Superset:", x.issuperset(y))
"""
Superset: False
Superset: True
"""