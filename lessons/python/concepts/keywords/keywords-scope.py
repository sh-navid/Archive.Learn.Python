# Local, NonLocal and Global

g = "global"


def f1():
    global g
    g += " value"
    print("In:\t", g)


f1()
print("Out:\t", g)

# Output:
"""
In:      global value
Out:     global value
"""


# -----------------------------

g = "global"


def f2():
    # g += " value" # -> UnboundLocalError: local variable 'g' referenced before assignment
    g = "local"
    print("In:\t", g)


f2()
print("Out:\t", g)

# Output:
"""
In:      local
Out:     global
"""


# -----------------------------

g = "global"


def f3():
    x = "local"
    print("In:\t", x)


f3()
# print("Out:\t", x)

# Output:
"""
In:      local
NameError: name 'x' is not defined
"""

# -----------------------------


def f4():
    s = "Hello"

    def inner():
        s = "Goodbye"
        print("Inner:", s)

    inner()

    print("Outer:", s)


f4()

# Output:
"""
Inner: Goodbye
Outer: Hello
"""

# -----------------------------

def f4():
    s = "Hello"

    def inner():
        global s
        s = "Goodbye"
        print("Inner:", s)

    inner()

    print("Outer:", s)


f4()
# Output
"""
Inner: Goodbye
Outer: Hello
"""

# -----------------------------

def f4():
    s = "Hello"

    def inner():
        nonlocal s # not local and not global
        s = "Goodbye"
        print("Inner:", s)

    inner()

    print("Outer:", s)


f4()
# Output
"""
Inner: Goodbye
Outer: Goodbye
"""