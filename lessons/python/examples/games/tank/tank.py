## python -m pip install pygame
from math import radians, sin, cos
import pygame
import sys

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Config:
    W, H = 500, 500


img = pygame.image.load(sys.path[0] + "/tank.png")


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Player:
    x, y = Config.W // 2, Config.H // 2
    x_movement, y_movement = 8, 8
    radius = 10
    color = (255, 255, 255)
    angle = 0
    rotate_speed = 10

    def move_up(self):
        self.y -= self.y_movement
        self.update_rotation(0)

    def move_down(self):
        self.y += self.y_movement
        self.update_rotation(180)

    def move_left(self):
        self.x -= self.x_movement
        self.update_rotation(90)

    def move_right(self):
        self.x += self.x_movement
        self.update_rotation(270)

    def update_rotation(self,deg):
        if self.angle>360:
            self.angle-=360
            
        if self.angle<deg:
            self.angle+=self.rotate_speed
        elif self.angle>deg:
            self.angle-=self.rotate_speed
        
            

    def draw(self, screen):
        tank = pygame.transform.rotate(img, self.angle)
        size = tank.get_rect().size
        screen.blit(tank, (player.x - size[0] // 2, player.y - size[1] // 2))

        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

        nx, ny = (
            self.x + self.radius * sin(radians(self.angle)),
            self.y + self.radius * cos(radians(self.angle)),
        )
        pygame.draw.circle(screen, self.color, (nx, ny), self.radius // 2)


player = Player()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
screen = pygame.display.set_mode((Config.W, Config.H))
pygame.display.set_caption("Tank Game")
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

    clock.tick(60)
    screen.fill((30, 30, 30))
    player.draw(screen)
    pygame.display.update()
