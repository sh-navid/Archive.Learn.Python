import pygame

screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()


class Ball:
    def __init__(self, x, y, size) -> None:
        self.x = x
        self.y = y
        self.size = size

        if x == y:
            self.color = "white"  # Answer 4 <-----

    x = 250
    y = 250
    size = 10
    color = "yellow"  # Answer 4 <-----


NUM = 5
OFFSET = 150
DISTANCE = 50
ball_list = []
for row in range(0, NUM):
    for col in range(0, NUM):
        ball_size = 25  # (row + col) + 1 # Answer 5 <-----
        ball_x = OFFSET + row * DISTANCE
        ball_y = OFFSET + col * DISTANCE
        ball_list.append(Ball(ball_x, ball_y, ball_size))


done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for ball in ball_list:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), ball.size)
    pygame.display.update()
