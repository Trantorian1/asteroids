import random

import pygame

import circleshape
import constants
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.parent = id(self)

    def split(self):
        self.kill()

        if self.radius == constants.ASTEROID_MIN_RADIUS:
            return

        radius_new = self.radius - constants.ASTEROID_MIN_RADIUS
        angle = random.uniform(20, 50)
        velocity_1 = self.position.rotate(angle) * constants.ASTEROID_SPEED_INCREASE
        velocity_2 = self.position.rotate(-angle) * constants.ASTEROID_SPEED_INCREASE

        a1 = Asteroid(self.position.x, self.position.y, radius_new)
        a2 = Asteroid(self.position.x, self.position.y, radius_new)

        a1.velocity = velocity_1
        a2.velocity = velocity_2
        a1.parent = id(self)
        a2.parent = id(self)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt


class AsteroidField(pygame.sprite.Sprite):
    containers: list[pygame.sprite.Group]
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
