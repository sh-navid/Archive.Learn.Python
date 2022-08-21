# [Assignment Operators]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x = 4
print("x = 4")
print("x =", x, "Assignment")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x += 4
print("x += 4")
print("x =", x, "Addition")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x -= 4
print("x -= 4")
print("x =", x, "Subtraction")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x *= 4
print("x *= 4")
print("x =", x, "Multiplication")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x /= 4
print("x /= 4")
print("x =", x, "Division")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x //= 4
print("x //= 4")
print("x =", x, "Floor division")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x **= 4
print("x **= 4")
print("x =", x, "Exponentiation")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = 10
print("x =", x)
x %= 4
print("x %= 4")
print("x =", x, "Modulus")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1     &     1     ->    1     AND
# 1     &     0     ->    0     AND
# 0     &     1     ->    0     AND
# 0     &     0     ->    0     AND

# 10  -> 1010
# 04  -> 0100
# AND -> 0000 -> 0
x = 10
print("x =", x)
x &= 4
print("x &= 4")
print("x =", x, "AND")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1     |     1     ->    1     XOR
# 1     |     0     ->    1     XOR
# 0     |     1     ->    1     XOR
# 0     |     0     ->    0     XOR

# 10  -> 1010
# 04  -> 0100
# OR  -> 1110 -> 14
x = 10
print("x =", x)
x |= 4
print("x |= 4")
print("x =", x, "OR")
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1     ^     1     ->    0     XOR
# 1     ^     0     ->    1     XOR
# 0     ^     1     ->    1     XOR
# 0     ^     0     ->    0     XOR

# 10  -> 1010
# 04  -> 0100
# XOR -> 1110 -> 14
x = 10
print("x =", x)
x ^= 4
print("x ^= 4")
print("x =", x, "XOR")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
x = 10
x = 4
x = 4   Assignment

x = 10
x += 4
x = 14  Addition

x = 10
x -= 4
x = 6   Subtraction

x = 10
x *= 4
x = 40  Multiplication

x = 10
x /= 4
x = 2.5 Division

x = 10
x //= 4
x = 2   Floor division

x = 10
x **= 4
x = 10000 Exponentiation

x = 10
x %= 4
x = 2   Modulus

x = 10
x &= 4
x = 0   AND

x = 10
x |= 4
x = 14  OR

x = 10
x ^= 4
x = 14  XOR
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Advanced Coding [Optional]
"""
def calc(num, op, num2, name):
    global x
    x = int(num)
    print(f"x = {num}")
    print(f"x {op} {num2}, {name}")
    exec(f"x {op} {num2}", globals(), None)
    print(f"x = {x}\n")


calc(10, "=",   4, "Assignment")
calc(10, "+=",  4, "Addition")
calc(10, "-=",  4, "Subtraction")
calc(10, "*=",  4, "Multiplication")
calc(10, "/=",  4, "Division")
calc(10, "//=", 4, "Floor division")
calc(10, "**=", 4, "Exponentiation")
calc(10, "%=",  4, "Modulus")
calc(10, "&=",  4, "AND")
calc(10, "|=",  4, "OR")
calc(10, "^=",  4, "XOR")
"""
