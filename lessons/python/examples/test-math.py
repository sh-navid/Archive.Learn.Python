from math import ceil, factorial, floor, sqrt
from statistics import mean

## "math" is for float-numbers; "cmath" is for complex-numbers


print("ABS", abs(-100))
# ABS 100


print("Sqrt", sqrt(64))
# Sqrt 8.0


print("Ceil", ceil(64.4))
print("Floor", floor(64.4))
# Ceil 65
# Floor 64


print("Round", round(164.8))
print("Round", round(164.2))
# Round 165
# Round 164


print("max", max([1, 2, 3, 4, 5, 6]))
print("max", min([1, 2, 3, 4, 5, 6]))
print("mean", mean([1, 2, 3, 4, 5, 6]))
print("mean", mean([10, 20]))
# max    6
# max    1
# mean   3.5
# mean   15


print(factorial(3)) # 1*2*3     -> 6
print(factorial(5)) # 1*2*3*4*5 -> 120