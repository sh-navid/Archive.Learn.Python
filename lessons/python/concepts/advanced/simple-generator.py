# [Generator]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generate():
    for x in [1, 2, 3]:
        yield x * 2

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def generate_stages():
    import random

    yield "Stage 1"
    yield "Stage 2"
    if random.random() < 0.3:
        yield "Stage 3"
    if random.random() < 0.3:
        yield "Stage 4"
    if random.random() < 0.3:
        yield "Stage 5"

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
if __name__ == "__main__":
    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for x in generate():
        print(x, end="  ")
    print()

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    x = generate()
    print(x.__next__(), end="  ")
    print(x.__next__(), end="  ")
    print(x.__next__(), end="  ")
    print()

    ###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    for x in generate_stages():
        print(x, end="  ")
