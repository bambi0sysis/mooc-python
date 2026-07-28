import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
width, height = 640, 480

robot_img = pygame.image.load("robot.png")
r_width = robot_img.get_width()
r_height = robot_img.get_height()

x = y = 0

clock = pygame.time.Clock()

robots = []

for i in range(10):
    robots.append(
        {
            "x": random.randint(0, width - r_width),
            "y": -random.randint(0, height * 2),
            "falling": True,
        }
    )


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))
    for robot in robots:
        if robot["falling"]:
            robot["y"] += 1
            if robot["y"] >= height - r_height:
                robot["falling"] = False

        else:
            if robot["x"] <= width // 2:
                robot["x"] -= 1
            else:
                robot["x"] += 1

            if robot["x"] < -r_width or robot["x"] > width:
                robot["falling"] = True
                robot["x"] = random.randint(0, width - r_width)
                robot["y"] = -random.randint(100, 500)

    for r in robots:
        screen.blit(robot_img, (r["x"], r["y"]))
    pygame.display.flip()

    clock.tick(120)
