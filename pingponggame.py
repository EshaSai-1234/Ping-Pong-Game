import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up fonts
font = pygame.font.SysFont("Arial", 32)

# Paddle properties
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
paddle_speed = 15

# Ball properties
BALL_RADIUS = 15
ball_speed_x = 7
ball_speed_y = 7

# Initialize paddles and ball positions
left_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

# Set up the score
left_score = 0
right_score = 0

# Game loop
running = True
while running:
    pygame.time.delay(30)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move paddles
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.move_ip(0, paddle_speed)
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.move_ip(0, paddle_speed)

    # Move ball
    ball.move_ip(ball_speed_x, ball_speed_y)

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds (left or right)
    if ball.left <= 0:
        right_score += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        ball_speed_x = -ball_speed_x
    if ball.right >= WIDTH:
        left_score += 1
        ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        ball_speed_x = -ball_speed_x

    # Draw everything
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, left_paddle)
    pygame.draw.rect(win, WHITE, right_paddle)
    pygame.draw.circle(win, WHITE, ball.center, BALL_RADIUS)  # Ball as circle
    pygame.draw.rect(win, WHITE, pygame.Rect(WIDTH // 2 - 1, 0, 2, HEIGHT))  # middle line

    # Draw scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    win.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 20))
    win.blit(right_text, (WIDTH * 3 // 4 - right_text.get_width() // 2, 20))

    pygame.display.update()

# Quit pygame
pygame.quit()
