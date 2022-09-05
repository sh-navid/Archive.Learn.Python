a = 20
if a % 2 == 0 and a > 10:
    print("Hello")

# --------------------------------------------------
if a % 2 == 0 or a > 10:
    print("Hello")

# --------------------------------------------------
print("hello" in "hello world")
print("hello" not in "hello world")

# --------------------------------------------------
a = [1, 2, 3]
b = a.copy()
c=a
print("is:", a is b)
print("is:", a is c)
