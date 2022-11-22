# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = "Hello World"


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Slice: ", s[0:5])
# Slice:  Hello

print("Slice: ", s[2:4])
# Slice:  ll


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Split: ", s.split(" "))
# Split:  ['Hello', 'World']

print("Split: ", s.split("Wor"))
# Split:  ['Hello ', 'ld']


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("Partition: ", s.partition("l"))
# Partition:  ('He', 'l', 'lo World')

print("R-Partition: ", s.rpartition("l"))
# R-Partition:  ('Hello Wor', 'l', 'd')


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
s = """
    Hello
    To
    This
    World
"""
print("SplitLines: ", s.splitlines())
# SplitLines:  ['', '    Hello', '    To', '    This', '    World']