import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
width, height = 640, 480

ball = pygame.image.load("ball.png")
ball_width = ball.get_width()
ball_height = ball.get_height()

clock = pygame.time.Clock()
vx = vy = 1
x = y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    x += vx
    if x + ball_width >= width:
        vx = -vx
        x = width - ball_width
    elif x <= 0:
        vx = -vx
        x = 0
    y += vy
    if y + ball_height >= height:
        vy = -vy
        y = height - ball_height
    elif y <= 0:
        vy = -vy
        y = 0
    pygame.display.flip()
    clock.tick(120)
