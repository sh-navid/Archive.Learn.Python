# @property
# [Decorator]
# Add functionality to existing code

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def my_decorator(func):
    def inner(value):
        print("Decorator Called...")
        return func(value)

    return inner


@my_decorator
def my_function(value):
    print("Show:", value)


my_function(12)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def show_values_decorator(func):
    def inner(*args):
        print("\nThis is from show decorator:", args, args[0])
        return func(*args)

    return inner


def pow_values_decorator(func):
    def inner(*args):
        args = list(args)
        for i in range(len(args)):
            args[i] **= 2
        print("This is from pow decorator:", args, args[0])
        return func(*args)

    return inner


@show_values_decorator
@pow_values_decorator
def calc(*args):
    print("This is From Function:", args, args[0])


calc(1)
calc(1, 2)
calc(1, 2, 3, 4, 5)
