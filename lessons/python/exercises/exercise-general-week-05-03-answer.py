import pygame
from random import randint as r, choice as c

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


COLORS = [
    "green",
    "hotpink",
    "purple",
    "blue",
    "red",
    "gray",
    "yellow",
]


class Ball:
    # Answer 1,2 <-----
    def __init__(self, x=250, y=250, size=10, color=COLORS[0], no=-1):
        self.x, self.y = x, y
        self.size = size
        self.color = color
        self.no = no


# Answer 3 <-----
balls = []
for i in range(0, 10):
    ball = Ball(
        x=r(50, 450),
        y=r(50, 450),
        size=r(5, 40),
        color=c(COLORS),
        no=i,
    )
    balls.append(ball)


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Answer 2 <-----
    # my_ball1 = Ball(100, 100, 20, "pink")
    # my_ball2 = Ball(400)
    # my_ball3 = Ball(y=400, size=30)
    # my_ball4 = Ball(color="red")

    # pygame.draw.circle(screen, my_ball1.color, (my_ball1.x, my_ball1.y), my_ball1.size)
    # pygame.draw.circle(screen, my_ball2.color, (my_ball2.x, my_ball2.y), my_ball2.size)
    # pygame.draw.circle(screen, my_ball3.color, (my_ball3.x, my_ball3.y), my_ball3.size)
    # pygame.draw.circle(screen, my_ball4.color, (my_ball4.x, my_ball4.y), my_ball4.size)

    # Answer 3 <-----
    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)

    pygame.display.update()
