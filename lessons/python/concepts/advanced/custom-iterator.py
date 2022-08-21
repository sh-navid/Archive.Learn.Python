# [Custom Iterator]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class MyCustomIterator:
    # Constructor
    def __init__(self, min, max, step=1):
        self.min = min
        self.max = max
        self.step = step

    # Create Iterator
    def __iter__(self):
        return self

    def __next__(self):
        tmp = self.min
        self.min += self.step
        if tmp <= self.max:
            return tmp
        # return StopIteration
        raise StopIteration  # Important to raise it

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
i = MyCustomIterator(10, 20).__iter__()
while True:
    try:
        print(i.__next__())
    except StopIteration:
        print("End")
        break

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in MyCustomIterator(10, 30, step=4):
    # if i is StopIteration:
    #     break
    print(i)
