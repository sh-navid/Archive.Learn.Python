from contextlib import contextmanager
import sys

# --------------------------------------------------
address = sys.path[0] + "/keywords-raise.py"

# --------------------------------------------------
# "open" is a "ContextManager"
# "with" makes the exception handeling easy
with open(address, "r") as file:
    print("\n".join(file.readlines()))

# --------------------------------------------------
# Alternative to "with" for "open"
file = open(address, "r")
try:
    print("\n".join(file.readlines()))
finally:
    file.close()


# --------------------------------------------------
@contextmanager
def my_context_manager(name):  # Useless example; just for test
    name = name.upper()
    yield name


with my_context_manager("hello") as name:
    print(name)

# --------------------------------------------------
@contextmanager
def my_div_context_manager(a, b):  # Useless example; just for test
    try:
        yield a / b
    except:
        yield "Bad Input"


with my_div_context_manager(10, 0) as result:
    print(result)

# --------------------------------------------------
class MyMath(object):  # Useless example; just for test
    def __init__(self):
        print("\nMyMath.__init__")

    def __enter__(self):
        print("MyMath.__enter__")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("MyMath.__exit__", exc_type, exc_value, traceback)
        return self

    def __del__(self):
        print("MyMath.__del__")

    def div(self, a, b):
        return a / b


with MyMath() as math:
    print(math.div(10, 10))
    print(math.div(20, 10))
    print(math.div(0, 10))
    print(math.div(10, 0))  # error
    print(math.div(10, 10))  # Not called
    print(math.div(20, 10))  # Not called
    print(math.div(30, 10))  # Not called

print("End of program")


## Read more from here:
# https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
# https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
# https://docs.python.org/2/reference/datamodel.html#with-statement-context-managers
# https://stackoverflow.com/questions/26907175/how-to-manipulate-the-exception-in-exit-of-a-context-manager
# https://www.geeksforgeeks.org/__exit__-in-python/
