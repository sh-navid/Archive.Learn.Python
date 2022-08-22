# Frozen Set

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Sets do not allow mutable objects but they are mutable in nature
my_set={1,2,3}
my_set.remove(1)
my_set.add(10)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Frozensets are immutable version of set and cannot be changed

my_frozen_set=frozenset({1,2,3})
print(my_frozen_set)
"""
frozenset({1, 2, 3})
"""

my_frozen_set=frozenset("Hello")
print(my_frozen_set)
"""
frozenset({'e', 'o', 'l', 'H'})
"""

my_frozen_set=frozenset({"a":1,"b":2})
print(my_frozen_set)
"""
frozenset({'a', 'b'})
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
my_frozen_set=frozenset({1,2,3})
my_frozen_set.add(10)
"""
AttributeError: 'frozenset' object has no attribute 'add'
"""