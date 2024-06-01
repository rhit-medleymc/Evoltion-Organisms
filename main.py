import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Platformer")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)

# Set up the player
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2 - player_width // 2, HEIGHT // 2 - player_height // 2
player_speed = 5
player_jump_power = -10
player_gravity = 0.5
is_jumping = False
jump_count = 10  # Number of frames the player can jump for

# Set up the stationary object
object_width, object_height = 100, 50
object_x, object_y = 400, HEIGHT - object_height
object_color = RED

# Set up game loop
clock = pygame.time.Clock()
running = True

# Set up camera
camera_x, camera_y = 0, 0

while running:
    clock.tick(60)  # 60 frames per second
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        jump_count = 10

    # Apply jumping
    if is_jumping:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            is_jumping = False
            jump_count = 10

    # Apply gravity
    player_y += player_gravity

    # Check for collisions with ground (simple ground at y=HEIGHT)
    if player_y >= HEIGHT - player_height:
        player_y = HEIGHT - player_height
        is_jumping = False

    # Update camera position to follow the player
    camera_x = player_x - WIDTH // 2
    camera_y = player_y - HEIGHT // 2

    # Update display
    win.fill(GREEN)  # Background color

    # Draw stationary object
    pygame.draw.rect(win, object_color, (object_x - camera_x, object_y - camera_y, object_width, object_height))

    # Draw player
    pygame.draw.rect(win, BLUE, (player_x - camera_x, player_y - camera_y, player_width, player_height))

    # Draw ground
    pygame.draw.rect(win, BROWN, (0, HEIGHT - camera_y, WIDTH, 20))

    pygame.display.flip()

pygame.quit()
sys.exit()
