# [Bitwise Operators]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calc(a, b, op, op_name):
    result = eval(f"{a}{op}{b}")
    print(f"{a}\t{op}\t{b}\t->\t{result}\t{op_name}".expandtabs(6))


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
calc(1, 1, "&", "AND")
calc(1, 0, "&", "AND")
calc(0, 1, "&", "AND")
calc(0, 0, "&", "AND")
print()

# 1     &     1     ->    1     AND
# 1     &     0     ->    0     AND
# 0     &     1     ->    0     AND
# 0     &     0     ->    0     AND

calc(1, 1, "|", "OR")
calc(1, 0, "|", "OR")
calc(0, 1, "|", "OR")
calc(0, 0, "|", "OR")
print()

# 1     |     1     ->    1     OR
# 1     |     0     ->    1     OR
# 0     |     1     ->    1     OR
# 0     |     0     ->    0     OR

calc(1, 1, "^", "XOR")  # Exclusive OR
calc(1, 0, "^", "XOR")
calc(0, 1, "^", "XOR")
calc(0, 0, "^", "XOR")
print()

# 1     ^     1     ->    0     XOR
# 1     ^     0     ->    1     XOR
# 0     ^     1     ->    1     XOR
# 0     ^     0     ->    0     XOR

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
calc(10, 4, "^", "XOR")

# 10    ^     4     ->    14    XOR

# How to calculate this?
# 10  -> 1010
# 04  -> 0100
# XOR -> 1110 -> 14

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Unary operator works only on one operator like -
# ~ unary bitwise complement operator -> bitwise one's complement operator
print(~0)  # -1
print(~1)  # -2

print(~10)  # -11 [DOUBLE CHECK THIS]!
# Sign Bit   -   Magnitude
# 0              0101       ->  +5
# 1              1010       ->  -5
# One's Complement: Inverting each bit
# Two's Complement: Inverting the bits and adding one
# ----------
# 10 -> 1010
# inv
# ----------
#       0101
#      +   1
# ----------
#       0110
print(int("0b0110", 2))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shift(a, op, b):
    op_name = "Left Shift"
    if op == ">>":
        op_name = "Right Shift"
    result = eval(f"{a}{op}{b}")
    print(f"{a} {op} {b} = {result}\t\t{bin(result)}\t\t{op_name}".expandtabs(10))


shift(10, "<<", 0)
shift(10, "<<", 1)
shift(10, "<<", 2)
shift(10, "<<", 3)
shift(10, "<<", 4)
shift(10, ">>", 1)
shift(10, ">>", 2)
shift(10, ">>", 3)
shift(10, ">>", 4)

"""
   OP     Decimal             Binary              Operator Name
------------------------
10 << 0 = 10                  0b1010              Left Shift
10 << 1 = 20                  0b10100             Left Shift
10 << 2 = 40                  0b101000            Left Shift
10 << 3 = 80                  0b1010000           Left Shift
10 << 4 = 160                 0b10100000          Left Shift
10 >> 1 = 5                   0b101               Right Shift
10 >> 2 = 2                   0b10                Right Shift
10 >> 3 = 1                   0b1                 Right Shift
10 >> 4 = 0                   0b0                 Right Shift
------------------------
"""
