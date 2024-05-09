import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Snake properties
block_size = 20
snake_speed = 10

# Font
font = pygame.font.SysFont(None, 40)

# Function to draw the snake
def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block_size, block_size])

# Function to display text on screen
def message(msg, color, score):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width / 6, height / 3])
    score_text = font.render(f"Your Score: {score}", True, "red")
    screen.blit(score_text, [10, 10])

# Main game function
def gameLoop():

    score = 0

    game_over = False
    game_close = False

    # Snake properties
    snake_list = []
    snake_length = 1
    snake_head = [width / 2, height / 2]
    snake_list.append(snake_head)

    # Fruit properties
    fruit_x = round(random.randrange(0, width - block_size) / 20.0) * 20
    fruit_y = round(random.randrange(0, height - block_size) / 20.0) * 20

    # Direction
    direction = 'RIGHT'
    change_to = direction

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            screen.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red, score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    change_to = 'DOWN'

        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        elif change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        elif change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        elif change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'

        if direction == 'LEFT':
            snake_head[0] -= block_size
        elif direction == 'RIGHT':
            snake_head[0] += block_size
        elif direction == 'UP':
            snake_head[1] -= block_size
        elif direction == 'DOWN':
            snake_head[1] += block_size

        if snake_head[0] >= width:
            snake_head[0] = 0
        elif snake_head[0] < 0:
            snake_head[0] = width - block_size
        elif snake_head[1] >= height:
            snake_head[1] = 0
        elif snake_head[1] < 0:
            snake_head[1] = height - block_size

        if snake_head in snake_list[:-1]:
            game_close = True

        snake_list.append(list(snake_head))
        if len(snake_list) > snake_length:
            del snake_list[0]

        screen.fill(white)
        pygame.draw.rect(screen, red, [fruit_x, fruit_y, block_size, block_size])

        draw_snake(snake_list)
        pygame.display.update()

        if snake_head[0] == fruit_x and snake_head[1] == fruit_y:
            fruit_x = round(random.randrange(0, width - block_size) / 20.0) * 20
            fruit_y = round(random.randrange(0, height - block_size) / 20.0) * 20
            score += 1
            snake_length += 1

        clock.tick(snake_speed)

gameLoop()
