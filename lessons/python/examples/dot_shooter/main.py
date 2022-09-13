## python -m pip install pygame
from math import radians, sin, cos
import pygame

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Config:
    W, H = 700, 700


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Player:
    x, y = Config.W // 2, Config.H // 2
    x_movement, y_movement = 8, 8
    radius = 15
    color = (255, 255, 255)
    angle = 0
    rotate_speed = 5

    def move_up(self):
        self.y -= self.y_movement

    def move_down(self):
        self.y += self.y_movement

    def move_left(self):
        self.x -= self.x_movement

    def move_right(self):
        self.x += self.x_movement

    def rotate_left(self):
        self.angle += self.rotate_speed

    def rotate_right(self):
        self.angle -= self.rotate_speed

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        nx, ny = (
            self.x + self.radius * sin(radians(self.angle)),
            self.y + self.radius * cos(radians(self.angle)),
        )
        pygame.draw.circle(screen, self.color, (nx, ny), self.radius // 2)


player = Player()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
screen = pygame.display.set_mode((Config.W, Config.H))
pygame.display.set_caption("Dot Shooter")
clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move_left()
    if keys[pygame.K_RIGHT]:
        player.move_right()
    if keys[pygame.K_UP]:
        player.move_up()
    if keys[pygame.K_DOWN]:
        player.move_down()
    if keys[pygame.K_d]:
        player.rotate_right()
    if keys[pygame.K_a]:
        player.rotate_left()

    clock.tick(60)
    screen.fill((0, 0, 0))
    player.draw()
    pygame.display.update()
