## python -m pip install pygame
import pygame
import random

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Our Simple Game Part3")
clock = pygame.time.Clock()

x, y = 250, 250
nx, ny = None, None
speed = 5
nSpeed= 10

while True:
    clock.tick(60)  # 60 frames per seccond
    screen.fill((255, 0, 127))

    if nx is None and ny is None:
        nx = random.randint(0, 500)
        ny = random.randint(0, 500)

    if nSpeed is None:
        nSpeed=random.randint(1, 30)

    if nx is not None:
        if x < nx - speed:
            x += speed
        elif x > nx + speed:
            x -= speed
        else:
            x = nx
            nx = None

    if ny is not None:
        if y < ny - speed:
            y += speed
        elif y > ny + speed:
            y -= speed
        else:
            y = ny
            ny = None

    if nSpeed is not None:
        if speed<nSpeed:
            speed+=1
        elif speed>nSpeed:
            speed-=1
        else:
            speed=nSpeed
            nSpeed=None


    pygame.draw.circle(screen, (127, 255, 0), (x, y), 10)
    pygame.display.update()
