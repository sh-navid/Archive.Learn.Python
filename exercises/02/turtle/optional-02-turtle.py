import turtle
import random

# چه تغییری در این برنامه میتونید اعمال کنید؟

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ts = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for t in ts:
    t.speed(200)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = +10
y = -10

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(800):
    ts[0].forward(x)
    ts[0].right(y)
    ts[1].forward(-x)
    ts[1].right(y)
    ts[2].forward(x)
    ts[2].right(-y)
    ts[3].forward(-x)
    ts[3].right(-y)

    if random.choice([True, False]):
        y = -y
    if random.choice([True, False]):
        x = -x
    if random.random() < 0.1:
        x = random.randint(10, 30)
    if random.random() < 0.1:
        x = random.randint(10, 30)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
turtle.done()
