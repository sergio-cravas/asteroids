import sys
import pygame

from shot import Shot 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH 

from logger import log_state, log_event

def main():
    print(f"Starting Asteroids")

    dt: float = 0.0
    shoots = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shoots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    screen = init_screen()
    player = init_player()
    field = AsteroidField()
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

        for asteroid in asteroids:
            for shot in shoots:
                if (asteroid.collides_with(shot)): 
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                
            if (asteroid.collides_with(player)): 
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        pygame.display.flip()


def init_screen():
    pygame.init()
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def init_player():
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


if __name__ == "__main__":
    main()
