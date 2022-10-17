class Counter:
    __counter = 0  # Private member

    def inc(self):
        self.__counter += 1

    def dec(self):
        self.__counter -= 1

    def reset(self):
        self.__counter = 0

    def __str__(self) -> str:
        return str(self.__counter)


counter1 = Counter()
print(counter1)
counter1.inc()
print(counter1)
counter1.reset()
print(counter1)

# print(counter1.__counter) #AttributeError: 'Counter' object has no attribute '__counter'
