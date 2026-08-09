import pygame
import random

pygame.init()
screen = pygame.display.set_mode((640, 480))
width, height = 640, 480

# Assets
robot_img = pygame.image.load("robot.png")
rock_img = pygame.image.load("rock.png")  # Load the rock image

r_w = robot_img.get_width()
r_h = robot_img.get_height()
# Assuming rock is similar size, but good to get its dimensions if needed
rock_w = rock_img.get_width()
rock_h = rock_img.get_height()

# 1. Player State (Only moves Left/Right at the bottom)
player_x = width // 2 - r_w // 2
player_y = height - r_h
player_speed = 5

# 2. Asteroid State (Start with just ONE to keep it simple)
asteroids = []
asteroids.append(
    {
        "x": random.randint(0, width - rock_w),
        "y": -100,  # Start above screen
        "speed": 3,
    }
)

# 3. Game State
score = 0
game_state = "playing"  # or "game_over"
font = pygame.font.SysFont("Arial", 30)

clock = pygame.time.Clock()

while True:
    # --- EVENT HANDLING ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # Restart logic
        if game_state == "game_over" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                score = 0
                asteroids = [
                    {"x": random.randint(0, width - rock_w), "y": -100, "speed": 3}
                ]
                game_state = "playing"

    # --- GAME LOGIC (Only run if playing) ---
    keys = pygame.key.get_pressed()

    if game_state == "playing":
        # 1. Move Player
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - r_w:
            player_x += player_speed

        # 2. Move Asteroids & Check Collisions
        for ast in asteroids:
            ast["y"] += ast["speed"]

            # CHECK 1: Did player catch it? (AABB Collision)
            # Note: We use rock_w/h for the asteroid bounds
            if (
                player_x < ast["x"] + rock_w
                and player_x + r_w > ast["x"]
                and player_y < ast["y"] + rock_h
                and player_y + r_h > ast["y"]
            ):
                score += 1
                asteroids.remove(ast)  # Remove caught asteroid
                # Add a new one immediately
                asteroids.append(
                    {
                        "x": random.randint(0, width - rock_w),
                        "y": -100,
                        "speed": 3 + score // 5,
                    }
                )
                break  # Break loop since list changed

            # CHECK 2: Did it hit the ground? (GAME OVER)
            elif ast["y"] > height:
                game_state = "game_over"

    # --- DRAWING ---
    screen.fill((0, 0, 0))

    # Draw Player
    screen.blit(robot_img, (player_x, player_y))

    # Draw Asteroids (Now using rock_img)
    for ast in asteroids:
        screen.blit(rock_img, (ast["x"], ast["y"]))

    # Draw Score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw Game Over
    if game_state == "game_over":
        over_text = font.render("GAME OVER! Press SPACE", True, (255, 0, 0))
        text_rect = over_text.get_rect(center=(width // 2, height // 2))
        screen.blit(over_text, text_rect)

    pygame.display.flip()
    clock.tick(60)
