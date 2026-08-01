import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
width, height = 640, 480

robot = pygame.image.load("robot.png")
x = 0
y = height - robot.get_height()

to_right = False
to_left = False
to_UP = False
to_DOWN = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_UP = True
            if event.key == pygame.K_DOWN:
                to_DOWN = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_UP = False
            if event.key == pygame.K_DOWN:
                to_DOWN = False

        if event.type == pygame.QUIT:
            exit()

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_UP:
        y -= 2
    if to_DOWN:
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
