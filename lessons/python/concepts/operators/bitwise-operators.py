# [Bitwise Operators]

import numpy as np

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
# Unary operator works only on one operator like ~
# ~ bitwise one's complement operator
print(~0)  # -1
print(~1)  # -2

print(~10)  # -11
# Sign Bit   -   Magnitude
# 0              0101       ->  +5
# 1              1010       ->  -5
# One's Complement: Inverting each bit                |-> One's 5 = -6
# Two's Complement: Inverting the bits and adding one |-> Two's 5 = -5
print("One's 12 ->",~12) # One's 12 -> -13

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def shift(a, op, b):
    op_name = "Left Shift"
    if op == ">>":
        op_name = "Right Shift"
    result = eval(f"{a}{op}{b}")
    print(f"{a} {op} {b} = {result}\t\t{np.binary_repr(result).zfill(8)}\t\t{op_name}".expandtabs(10))


shift(10, "<<", 0)
shift(10, "<<", 1)
shift(10, "<<", 2)
shift(10, "<<", 3)
shift(10, "<<", 4)
shift(10, "<<", 5)
shift(10, "<<", 6)
shift(10, ">>", 0)
shift(10, ">>", 1)
shift(10, ">>", 2)
shift(10, ">>", 3)
shift(10, ">>", 4)

"""
   OP     Decimal             Binary              Operator Name
------------------------
10 << 0 = 10                  00001010            Left Shift
10 << 1 = 20                  00010100            Left Shift
10 << 2 = 40                  00101000            Left Shift
10 << 3 = 80                  01010000            Left Shift
10 << 4 = 160                 10100000            Left Shift
10 << 5 = 320                 101000000           Left Shift
10 << 6 = 640                 1010000000          Left Shift
------------------------
10 >> 0 = 10                  00001010            Right Shift
10 >> 1 = 5                   00000101            Right Shift
10 >> 2 = 2                   00000010            Right Shift
10 >> 3 = 1                   00000001            Right Shift
10 >> 4 = 0                   00000000            Right Shift
------------------------
"""
