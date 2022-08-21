## python -m pip install pygame
import pygame
import random

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Our Simple Game Part1")
clock = pygame.time.Clock()

while True:
    clock.tick(5)  # 5 frames per seccond
    screen.fill((255, 0, 127))

    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pygame.draw.circle(screen, (127, 255, 0), (x, y), 10)

    pygame.display.update()
