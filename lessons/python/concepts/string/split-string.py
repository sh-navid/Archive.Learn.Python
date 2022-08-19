s = "Hello World"


print("Slice: ", s[0:5])
print("Slice: ", s[2:4])


print("Split: ", s.split(" "))
print("Split: ", s.split("Wor"))


print("Partition: ", s.partition("l"))
print("R-Partition: ", s.rpartition("l"))


s = """
    Hello
    To
    This
    World
"""
print("SplitLines: ", s.splitlines())
