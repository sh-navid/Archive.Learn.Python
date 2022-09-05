def div(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot devide by zero")
        #raise Exception("You cannot devide by zero")
    print(a / b)


try:
    div(1, 0)
except ZeroDivisionError as z:
    print(z)
