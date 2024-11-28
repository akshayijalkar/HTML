import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 600

# Create the game window
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Colors
background_color = (135, 206, 235)  # Sky blue
bird_color = (255, 255, 0)  # Yellow
pipe_color = (34, 139, 34)  # Green
ground_color = (139, 69, 19)  # Brown

# Game variables
bird_position = [100, 300]  # Initial bird position (x, y)
bird_radius = 15  # Bird size
bird_velocity = 0  # Bird's vertical velocity
gravity = 0.5  # Downward acceleration
jump_strength = -10  # Upward force when jumping
pipe_width = 50
pipe_gap = 150
pipe_speed = 3
score = 0
game_over = False

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Function to display the score
def display_score(current_score):
    score_text = font.render(f"Score: {current_score}", True, (0, 0, 0))
    game_screen.blit(score_text, (10, 10))

# Create initial pipes
pipes = [
    {"x": 400, "height": random.randint(100, 400)}
]

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength  # Jump when spacebar is pressed

    # Background and ground
    game_screen.fill(background_color)
    pygame.draw.rect(game_screen, ground_color, (0, screen_height - 50, screen_width, 50))

    if not game_over:
        # Bird mechanics
        bird_velocity += gravity
        bird_position[1] += bird_velocity
        pygame.draw.circle(game_screen, bird_color, bird_position, bird_radius)

        # Pipe mechanics
        for pipe in pipes:
            pipe["x"] -= pipe_speed
            pygame.draw.rect(game_screen, pipe_color, (pipe["x"], 0, pipe_width, pipe["height"]))
            pygame.draw.rect(
                game_screen, 
                pipe_color, 
                (pipe["x"], pipe["height"] + pipe_gap, pipe_width, screen_height - pipe["height"] - pipe_gap - 50)
            )
            # Check for collision
            if (
                bird_position[0] + bird_radius > pipe["x"] and
                bird_position[0] - bird_radius < pipe["x"] + pipe_width and
                (bird_position[1] - bird_radius < pipe["height"] or 
                 bird_position[1] + bird_radius > pipe["height"] + pipe_gap)
            ):
                game_over = True

            # Check if pipe is off-screen and add a new one
            if pipe["x"] + pipe_width < 0:
                pipes.remove(pipe)
                pipes.append({"x": 400, "height": random.randint(100, 400)})
                score += 1

        # Check for ground or ceiling collision
        if bird_position[1] + bird_radius > screen_height - 50 or bird_position[1] - bird_radius < 0:
            game_over = True

        # Display score
        display_score(score)
    else:
        # Display game over message
        game_over_text = font.render("Game Over! Press R to Restart", True, (0, 0, 0))
        game_screen.blit(game_over_text, (50, screen_height // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:  # Restart game
            bird_position = [100, 300]
            bird_velocity = 0
            pipes = [{"x": 400, "height": random.randint(100, 400)}]
            score = 0
            game_over = False

    # Update the screen
    pygame.display.flip()
    clock.tick(30)
