import time
import pygame
import random

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Dodge")

game_bgm = pygame.mixer.music.load("DodgeSong.mp3")
pygame.mixer.music.play(-1)
# pygame.mixer.music.set_volume(0.5)  # Set volume of background music (0.0 - 1.0)
ending_track = pygame.mixer.Sound("endingTrack.mp3")
ending_track.set_volume(0.7)  # Set volume of ending track

# BG = pygame.image.load("space_bg.jpg")s
# BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 40
PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, stars, player_score, game_level):
    WINDOW.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    level_score = FONT.render(f"Level: {game_level}", 1, "white")
    score_text = FONT.render(f"Score: {player_score}", 1, "white")
    WINDOW.blit(time_text, (10, 10))
    WINDOW.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
    WINDOW.blit(level_score, (WIDTH - score_text.get_width() - 10, score_text.get_height()+10))
    pygame.draw.rect(WINDOW, (255, 0, 0), player)

    for star in stars:
        pygame.draw.rect(WINDOW, "white", star)

    pygame.display.update()


def main():

    run = True
    # Rect(block_x_location, block_y_location, block_height, block_width)
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    loop_clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    player_score = 0
    game_level = 0
    level_check = 0
    star_add_increment = 2000 # ms
    star_count = 0
    stars = []

    hit = False

    while run:
        # pygame.mixer.music.play(-1)
        star_count += loop_clock.tick(60)  # To update every second
        elapsed_time = time.time() - start_time

        # Generate 3 random stars
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(500, star_add_increment - 50)
            star_count = 0
            if star_add_increment % 4 == 0:
                game_level += 1

        # Events in pygame are mouse movements, key presses, etc in a pygame.display window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If hit close button in pygame window
                # pygame.quit()
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
                player_score += 1
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                player_score += 1
                hit = True
                break

        if hit:
            pygame.mixer.music.stop()  # Stop the main bg music
            ending_track.play()

            lost_text = FONT.render("You Lost", 1, "white")
            score_text = FONT.render(f"Your Score: {player_score}", 1, "white")
            WINDOW.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_width()/2))
            WINDOW.blit(score_text, (WIDTH/2 - lost_text.get_width()/2 - 20, HEIGHT/2 - lost_text.get_width()))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars, player_score, game_level)


    pygame.quit()

if __name__ == "__main__":
    main()
