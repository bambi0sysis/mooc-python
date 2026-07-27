import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
width, height = 640, 480

clock = pygame.time.Clock()

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

x = y = 0
velocity = 1
direction = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if direction == 0:
        x += velocity
        if x + robot_width > width:
            x = width - robot_width
            direction = 1
    elif direction == 1:
        y += velocity
        if y + robot_height > height:
            y = height - robot_height
            direction = 2
    elif direction == 2:
        x -= velocity
        if x < 0:
            x = 0
            direction = 3
    elif direction == 3:
        y -= velocity
        if y < 0:
            y = 0
            direction = 0

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(120)
