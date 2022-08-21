# [Iterator, Iterable]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# i             is iterator
# [2, 4, 6, 8]  is iterable
i = iter([2, 4, 6, 8])
print(next(i))  # Same as i.__next__()
print(next(i))
print(next(i))
print(next(i))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
i = iter([20, 40, 60, 80])
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
i = iter([200, 400, 600, 800])
while True:
    try:
        print(i.__next__())
    except StopIteration:
        print("End of list")
        break