# Boolean

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = True
print(b, type(b))
# True <class 'bool'>

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = False
print(b, type(b))
# False <class 'bool'>

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if True:
    print("This is True")
# This is True

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if False:
    print("This is False")

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = True
if b:
    print("B is True", type(b))
# B is True <class 'bool'>

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = 10 > 5
print(b, type(b))
# True <class 'bool'>

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b = len("Hello") == 5
print(b, type(b))
# True <class 'bool'>

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("False  and  False  ->", False and False)
print("True   and  False  ->", True and False)
print("False  and  True   ->", False and True)
print("True   and  True   ->", True and True)
print()

# False  and  False  -> False
# True   and  False  -> False
# False  and  True   -> False
# True   and  True   -> True
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("False  or  False  ->", False or False)
print("True   or  False  ->", True or False)
print("False  or  True   ->", False or True)
print("True   or  True   ->", True or True)
print()

# False  or  False  -> False
# True   or  False  -> True
# False  or  True   -> True
# True   or  True   -> True
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print("not True  ->", not True)
print("not False ->", not False)

# not True  -> False
# not False -> True
