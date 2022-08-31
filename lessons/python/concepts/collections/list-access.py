# [List]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print([], type([]))
print((), type(()))
print({}, type({}))
print({"x", "y"}, type({"x", "y"}))
print(frozenset({"x", "y"}), type(frozenset({"x", "y"})))
# Output
"""
[] <class 'list'>
() <class 'tuple'>
{} <class 'dict'>
{'y', 'x'} <class 'set'>
frozenset({'y', 'x'}) <class 'frozenset'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(list((1, 2, 3)))
print(tuple((1, 2, 3)))
print(set((1, 2, 3)))
print(frozenset((1, 2, 3)))
print(dict(key=12, test=True))
# Output:
"""
[1, 2, 3]
(1, 2, 3)
{1, 2, 3}
frozenset({1, 2, 3})
{'key': 12, 'test': True}
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Access Item
my_list = ["A", "B", "C"]
print("Access Item:", my_list[1], type(my_list))
"""
Access Item: B <class 'list'>
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# List Constructor (list)
my_list = list(("A", "B", "C"))
print("List:", my_list)
"""
List: ['A', 'B', 'C']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Change Item
my_list = ["A", "B", "C", "D", "E"]
my_list[1] = "Y"
print("Change Item [1]:", my_list)

my_list[1:3] = ["Q", "W"]
print("Change Item [1:3]:", my_list)

my_list[1:4] = ["Z", "X"]
print("Change Item [1:4]:", my_list)
"""
Change Item [1]: ['A', 'Y', 'C', 'D', 'E']
Change Item [1:3]: ['A', 'Q', 'W', 'D', 'E']
Change Item [1:4]: ['A', 'Z', 'X', 'E']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Loop, Iterate
my_list = ["A", "B", "C"]
for i in my_list:
    print("Loop:", i)
"""
Loop: A
Loop: B
Loop: C
"""

for i in range(len(my_list)):
    print(f"Loop {i}:", my_list[i])
"""
Loop 0: A
Loop 1: B
Loop 2: C
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Append
my_list = ["A", "B", "C"]
my_list.append("D")
print("Append:", my_list)
"""
Append: ['A', 'B', 'C', 'D']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Insert
my_list = ["A", "B", "C"]
my_list.insert(1, "D")
print("Insert:", my_list)
"""
Append: ['A', 'B', 'C', 'D']
Insert: ['A', 'D', 'B', 'C']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Remove
my_list = ["A", "B", "C"]
my_list.remove("B")
print("Remove:", my_list)
"""
Remove: ['A', 'C']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Delete
my_list = ["A", "B", "C"]
del my_list[0]
print("Delete:", my_list)
"""
Delete: ['B', 'C']
"""

del my_list
# print(my_list)
"""
NameError: name 'my_list' is not defined
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pop
my_list = ["A", "B", "C"]
print("Pop(1):", my_list.pop(1), my_list)
print("Pop():", my_list.pop(), my_list)
"""
Pop(1): B ['A', 'C']
Pop(): C ['A']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Copy with method / Copy with list constructor
my_list = ["A", "B", "C"]
my_list2 = my_list
my_list3 = list(my_list)
my_list4 = my_list.copy()
print("Is my_list the same as my_list2?", my_list is my_list2)
print("Is my_list the same as my_list3?", my_list is my_list3)
print("Is my_list the same as my_list4?", my_list is my_list4)
"""
Is my_list the same as my_list2? True
Is my_list the same as my_list3? False
Is my_list the same as my_list4? False
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Extend
my_list = ["A", "B", "C"]
my_list.extend(["K", "F"])
print("Extend:", my_list)
"""
Extend: ['A', 'B', 'C', 'K', 'F']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Clear
my_list = ["A", "B", "C"]
my_list.clear()
print("Clear:", my_list)
"""
Clear: []
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Len
print("Length:", ["A", "B", "C"].__len__())
print("Length:", len(["A", "B", "C"]))
"""
Length: 3
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Count
print("Count:", ["A", "B", "C", "C", "c"].count("C"))
"""
Count: 2
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Slice
my_list = ["A", "B", "C", "D", "E", "F", "G", "H"]
print("my_list[-1]    ", my_list[-1])
print("my_list[1]     ", my_list[1])
print("my_list[1:]    ", my_list[1:])
print("my_list[:4]    ", my_list[:4])
print("my_list[1:4]   ", my_list[1:4])
print("my_list[-5:-3] ", my_list[-5:-3])
"""
my_list[-1]     H
my_list[1]      B
my_list[1:]     ['B', 'C', 'D', 'E', 'F', 'G', 'H']
my_list[:4]     ['A', 'B', 'C', 'D']
my_list[1:4]    ['B', 'C', 'D']
my_list[-5:-3]  ['D', 'E']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Join
print("Join:", ["A", "B", "C"] + ["A", "B", "C"])
"""
Join: ['A', 'B', 'C', 'A', 'B', 'C']
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unpack
my_list = ["A", "B", "C"]
x, y, z = my_list
print("Unpack:", x, y, z)
"""
Unpack: A B C
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Check (in)
my_list = ["A", "B", "C"]
print("Is 'C' in my_list?", "C" in my_list)
print("Is 'K' in my_list?", "K" in my_list)
"""
Is 'C' in my_list? True
Is 'K' in my_list? False
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Index
my_list = ["A", "B", "C"]
print("Index:", my_list.index("B"))
"""
Index: 1
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Reverse
my_list = ["A", "B", "C"]
my_list.reverse()
print("Reverse:", my_list)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Sort -> is case sensitive by default -> first capital letters then lower ones
my_list = ["base", "Act", "ant", "car", "Book", "Cap"]
my_list.sort()
print("Sort:", my_list)
"""
Sort: ['Act', 'Book', 'Cap', 'ant', 'base', 'car']
"""

# Remove Sensitivity From Sort Function
my_list = ["base", "Act", "ant", "car", "Book", "Cap"]
my_list.sort(key=str.lower)
print("Sort:", my_list)
"""
Sort: ['Act', 'ant', 'base', 'Book', 'Cap', 'car']
"""

# Custom Sort Function
def my_custom_sort_function(item):
    return item[::-1]  # reverse string


my_list = ["base", "Act", "ant", "car", "Book", "Cap"]
my_list.sort(key=my_custom_sort_function)
print("Sort:", my_list)
"""
Sort: ['base', 'Book', 'Cap', 'car', 'Act', 'ant']
"""
