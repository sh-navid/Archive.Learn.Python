# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("".join(["A", "B", "C"]))
# ABC


print(",".join(["A", "B", "C"]))
# A,B,C


print(" --- ".join(["A", "B", "C"]))
# A --- B --- C


print(" --- ".join("Hello World"))
# H --- e --- l --- l --- o ---   --- W --- o --- r --- l --- d


print(" --- ".join("Hello World".split("W")))
# Hello  --- orld


print(" --- ".join("Hello World".partition("W")))
# Hello  --- W --- orld