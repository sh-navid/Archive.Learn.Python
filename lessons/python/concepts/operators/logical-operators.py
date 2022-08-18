# Logical
print("Logical")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def logical_and(a, b):
    print(f"{a}\tand\t{b}\t-> {a and b}")


logical_and(0, 0)
logical_and(0, 1)
logical_and(1, 0)
logical_and(1, 1)
print()

logical_and(False, False)
logical_and(False, True)
logical_and(True, False)
logical_and(True, True)
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def logical_or(a, b):
    print(f"{a}\tor\t{b}\t-> {a or b}")


logical_or(0, 0)
logical_or(0, 1)
logical_or(1, 0)
logical_or(1, 1)
print()

logical_or(False, False)
logical_or(False, True)
logical_or(True, False)
logical_or(True, True)
print()

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def logical_not(a):
    print(f"not {a}\t-> {not a}")

logical_not(0)
logical_not(1)
logical_not(False)
logical_not(True)


"""
0       and     0       -> 0
0       and     1       -> 0
1       and     0       -> 0
1       and     1       -> 1

False   and     False   -> False
False   and     True    -> False
True    and     False   -> False
True    and     True    -> True

0       or      0       -> 0
0       or      1       -> 1
1       or      0       -> 1
1       or      1       -> 1

False   or      False   -> False
False   or      True    -> True
True    or      False   -> True
True    or      True    -> True

not 0   -> True
not 1   -> False
not False       -> True
not True        -> False
"""