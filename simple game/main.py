import time
import pygame
import random

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# BG = pygame.image.load("space_bg.jpg")
# BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("space_gb.jpg"), (WIDTH, HEIGHT))



def draw():
    WINDOW.blit(BG, (0, 0))
    pygame.display.update()

def main():

    run = True
    while run:
        # Events in pygame are mouse movements, key presses, etc in a pygame.display window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If hit close button in pygame window
                # pygame.quit()
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()