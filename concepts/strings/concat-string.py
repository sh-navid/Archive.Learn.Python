# join, concatenation

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Join
print("".join(["A", "B", "C"]))
print(",".join(["A", "B", "C"]))
print(" --- ".join(["A", "B", "C"]))
print(" --- ".join("Hello World"))
print(" --- ".join("Hello World".split("W")))
print(" --- ".join("Hello World".partition("W")))

# ABC
# A,B,C
# A --- B --- C
# H --- e --- l --- l --- o ---   --- W --- o --- r --- l --- d
# Hello  --- orld
# Hello  --- W --- orld

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Concatenation
print("Hello" + " " + "World")

# Hello World
