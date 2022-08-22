## python -m pip install pygame
import pygame
import random

FPS = 60
SIZE = 500
BACKGROUND_COLOR = (255, 0, 127)


speed, nSpeed = 5, 10
clock = pygame.time.Clock()
circle_color = (127, 255, 0)
x, y, nx, ny = 250, 250, None, None
screen = pygame.display.set_mode((SIZE, SIZE))


pygame.display.set_caption("Our Simple Game Part4")


def choose_a_new_random_position_for_circle():
    global nx, ny
    if nx is None and ny is None:
        nx = random.randint(0, SIZE)
        ny = random.randint(0, SIZE)


def choose_a_random_speed_for_circle():
    if nSpeed is None:
        nSpeed = random.randint(1, 30)


def move_circle_in_x_direction():
    global x, nx
    if nx is not None:
        if x < nx - speed:
            x += speed
        elif x > nx + speed:
            x -= speed
        else:
            x = nx
            nx = None


def move_circle_in_y_direction():
    global y, ny
    if ny is not None:
        if y < ny - speed:
            y += speed
        elif y > ny + speed:
            y -= speed
        else:
            y = ny
            ny = None


def change_speed_of_circle_movement():
    global nSpeed, speed
    if nSpeed is not None:
        if speed < nSpeed:
            speed += 1
        elif speed > nSpeed:
            speed -= 1
        else:
            speed = nSpeed
            nSpeed = None


def change_color_of_circle():
    global circle_color
    circle_color = (
        random.randint(100, 255),
        random.randint(100, 255),
        random.randint(100, 255),
    )


while True:
    clock.tick(FPS)
    screen.fill(BACKGROUND_COLOR)

    choose_a_new_random_position_for_circle()
    change_speed_of_circle_movement()
    move_circle_in_x_direction()
    move_circle_in_y_direction()
    change_color_of_circle()

    pygame.draw.circle(screen, circle_color, (x, y), random.randint(10,30))
    pygame.display.update()
