import pygame
import time
import random
pygame.font.init()

WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, WIDTH))

def draw():
    WIN.blit(BG, (0, 0))
    pygame.draw.circle(WIN, (255, 0, 0), (WIDTH//2, WIDTH//2), 10)
    pygame.display.update()



def main():
    run = True

    # Draw player that is in a circle shape
    # player = pygame.draw.circle(WIN, (255, 0, 0), (WIDTH//2, WIDTH//2), 10)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

if __name__ == "__main__":
    main()