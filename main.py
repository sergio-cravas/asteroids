import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids")

    dt: float = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    screen = init_screen()
    player = init_player()
    clock = pygame.time.Clock()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()


def init_screen():
    pygame.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def init_player():
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


if __name__ == "__main__":
    main()
