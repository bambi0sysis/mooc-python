import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))
width, height = 640, 480

robot = pygame.image.load("robot.png")
robot_w = robot.get_width()
robot_h = robot.get_height()

x = random.randint(0, width - robot_w)
y = random.randint(0, height - robot_h)


while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = random.randint(0, width - robot_w)
            y = random.randint(0, height - robot_h)

        window.fill((0, 0, 0))
        window.blit(robot, (x, y))
        pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()
