from random import randint
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

screen.fill((0, 0, 0))
for i in range(1000):
    screen.blit(robot, (randint(0, 640 - width), randint(0, 480 - height)))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
