import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PLAYER_PADDLE_X = 20
COMPUTER_PADDLE_X = WIDTH - PADDLE_WIDTH - 20
player_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
computer_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2
player_score = 0
computer_score = 0

# Define the ball
BALL_RADIUS = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = random.choice([-1, 1]) * 3
ball_speed_y = random.choice([-1, 1]) * 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Set the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player's paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle_y > 0:
        player_paddle_y -= 5
    if keys[pygame.K_DOWN] and player_paddle_y < HEIGHT - PADDLE_HEIGHT:
        player_paddle_y += 5

    # Move the computer's paddle
    if computer_paddle_y + PADDLE_HEIGHT // 2 < ball_y and computer_paddle_y < HEIGHT - PADDLE_HEIGHT:
        computer_paddle_y += 3
    elif computer_paddle_y + PADDLE_HEIGHT // 2 > ball_y and computer_paddle_y > 0:
        computer_paddle_y -= 3

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Handle ball collisions with walls
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_RADIUS:
        ball_speed_y *= -1

    # Handle ball collisions with paddles
    if ball_x <= PLAYER_PADDLE_X + PADDLE_WIDTH and player_paddle_y <= ball_y <= player_paddle_y + PADDLE_HEIGHT:
        ball_speed_x *= -1
    elif ball_x >= COMPUTER_PADDLE_X - BALL_RADIUS and computer_paddle_y <= ball_y <= computer_paddle_y + PADDLE_HEIGHT:
        ball_speed_x *= -1

    # Handle ball going out of bounds
    if ball_x < 0:
        computer_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = random.choice([-1, 1]) * 3
        ball_speed_y = random.choice([-1, 1]) * 3
    elif ball_x > WIDTH:
        player_score += 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_speed_x = random.choice([-1, 1]) * 3
        ball_speed_y = random.choice([-1, 1]) * 3

    # Clear the screen
    win.fill(BLACK)

    # Draw the paddles, ball, and scores
    pygame.draw.rect(win, WHITE, (PLAYER_PADDLE_X, player_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(win, WHITE, (COMPUTER_PADDLE_X, computer_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.circle(win, WHITE, (ball_x, ball_y), BALL_RADIUS)
    font = pygame.font.Font(None, 36)
    player_text = font.render("Player: " + str(player_score), True, WHITE)
    computer_text = font.render("Computer: " + str(computer_score), True, WHITE)
    win.blit(player_text, (20, 20))
    win.blit(computer_text, (WIDTH - computer_text.get_width() - 20, 20))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
