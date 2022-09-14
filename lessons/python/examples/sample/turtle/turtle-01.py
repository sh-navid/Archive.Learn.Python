import turtle
import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ts = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for t in ts:
    t.speed(200)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
x = +45
y = -45

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i in range(120):
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

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
turtle.done()