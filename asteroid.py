import random
import pygame

from circleshape import CircleShape 
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS

from logger import log_event


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        original_position = self.position


        self.kill()

        # Small asteroid
        if self.radius <= ASTEROID_MIN_RADIUS: return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        asteroid_01 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_01.velocity = self.velocity.rotate(angle) * 1.2

        asteroid_02 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid_02.velocity = self.velocity.rotate(angle * -1) * 1.2