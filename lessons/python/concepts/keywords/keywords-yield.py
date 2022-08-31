def generator():
    yield 10
    yield 30
    yield 50

for x in generator():
    print(x)