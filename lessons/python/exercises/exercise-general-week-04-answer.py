from statistics import mean


l = list([2, 4, 6, 8, 10])
t = tuple([1, 3, 5, 7, 9, 10])
s = set([1, 2, 3, 10, 10, 10])
d = dict([("w1", 80), ("w2", 85), ("w3", 88)])

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer1
print(t + tuple(l))
"""(1, 3, 5, 7, 9, 10, 2, 4, 6, 8, 10)"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer2
mt = (1, 3, 5, 7, 9, 10, 2, 4, 6, 8, 10)
mt = set(mt)
mt = list(mt)
mt.sort()
print(tuple(mt))
"""(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer4
print(set(l).union(set(t)))
"""{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}"""

print(set(l).intersection(set(t)))
"""{10}"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer5 - First Way
m = mean(d.values())
print(m)
"""84.33333333333333"""

# Answer5 - Second Way
s = 0
for k, v in d.items():
    s += v
s /= len(d.items())
print(s)
"""84.33333333333333"""

# Answer5 - Third Way
s = sum([v for v in d.values()]) / len(d.items())
print(s)
"""84.33333333333333"""

# Answer5 - Another Way
s = 0
for v in d.values():
    s += v
s /= len(d.items())
print(s)
"""84.33333333333333"""

# Answer5 - Another Way
s = sum(d.values()) / len(d.items())
print(s)
"""84.33333333333333"""
