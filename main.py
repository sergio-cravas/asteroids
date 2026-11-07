import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids")

    screen = init_screen()
    clock = pygame.time.Clock()
    dt: float = 0.0

    player = init_player()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt = clock.tick(60) / 1000

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()


def init_screen():
    pygame.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def init_player():
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


if __name__ == "__main__":
    main()
