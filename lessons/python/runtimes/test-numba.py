## pip install numba
# JIT (Just-in-Time): Code compiles when it needed
# Numba: JIT compiler that translates a subset of Python and NumPy code into fast machine code. 
# It translates Python functions to optimized machine code at runtime.

from numba import jit


@jit
def numba_sum():
    sum = 0
    for i in range(100000000):
        sum += i
    print(sum)


numba_sum()


def sum():
    sum = 0
    for i in range(100000000):
        sum += i
    print(sum)


sum()

## Read more from here:
# https://numba.pydata.org/
