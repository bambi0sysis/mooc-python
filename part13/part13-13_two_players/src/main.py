import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
width, height = 640, 480

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()
x1 = 0
x2 = width - robot_width
y1 = 0
y2 = height - robot_height

r1_right = False
r1_left = False
r1_up = False
r1_down = False

r2_right = False
r2_left = False
r2_up = False
r2_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                r1_left = True
            if event.key == pygame.K_RIGHT:
                r1_right = True
            if event.key == pygame.K_UP:
                r1_up = True
            if event.key == pygame.K_DOWN:
                r1_down = True

            if event.key == pygame.K_a:
                r2_left = True
            if event.key == pygame.K_d:
                r2_right = True
            if event.key == pygame.K_w:
                r2_up = True
            if event.key == pygame.K_s:
                r2_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                r1_left = False
            if event.key == pygame.K_RIGHT:
                r1_right = False
            if event.key == pygame.K_UP:
                r1_up = False
            if event.key == pygame.K_DOWN:
                r1_down = False

            if event.key == pygame.K_a:
                r2_left = False
            if event.key == pygame.K_d:
                r2_right = False
            if event.key == pygame.K_w:
                r2_up = False
            if event.key == pygame.K_s:
                r2_down = False

        if event.type == pygame.QUIT:
            exit()

    if r1_right and x1 + 2 + robot_width <= width:
        x1 += 2
    if r1_left and x1 - 2 >= 0:
        x1 -= 2
    if r1_up and y1 - 2 >= 0:
        y1 -= 2
    if r1_down and y1 + 2 + robot_height <= height:
        y1 += 2

    if r2_right and x2 + 2 + robot_width <= width:
        x2 += 2
    if r2_left and x2 - 2 >= 0:
        x2 -= 2
    if r2_up and y2 - 2 >= 0:
        y2 -= 2
    if r2_down and y2 + 2 + robot_height <= height:
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
