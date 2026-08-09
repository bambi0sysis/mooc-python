import pygame
from datetime import datetime
import math

pygame.init()
window = pygame.display.set_mode((640, 480))
width, height = 640, 480


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    now = datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second
    pygame.display.set_caption(f"{hours}:{minutes}:{seconds}")
    window.fill((0, 0, 0))

    pygame.draw.circle(window, (255, 0, 0), (width / 2, height / 2), 10)
    pygame.draw.circle(window, (255, 0, 0), (width / 2, height / 2), 200, 5)

    sec_angle = (seconds / 60) * 2 * math.pi - math.pi / 2
    sec_x = width / 2 + 185 * math.cos(sec_angle)
    sec_y = height / 2 + 185 * math.sin(sec_angle)

    min_angle = ((minutes + seconds / 60) / 60) * 2 * math.pi - math.pi / 2
    min_x = width / 2 + 180 * math.cos(min_angle)
    min_y = height / 2 + 180 * math.sin(min_angle)

    hr_angle = ((hours % 12 + minutes / 60) / 12) * 2 * math.pi - math.pi / 2
    hr_x = width / 2 + 150 * math.cos(hr_angle)
    hr_y = height / 2 + 150 * math.sin(hr_angle)

    pygame.draw.line(window, (0, 0, 255), (width / 2, height / 2), (hr_x, hr_y), 4)
    pygame.draw.line(window, (0, 0, 255), (width / 2, height / 2), (min_x, min_y), 3)
    pygame.draw.line(window, (0, 0, 255), (width / 2, height / 2), (sec_x, sec_y), 2)

    pygame.display.flip()
