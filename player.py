import pygame

import circleshape
import constants


class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.__rotation: float = 0
        self.__shot_delay = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        right = pygame.Vector2(0, 1).rotate(self.__rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        if self.__shot_delay <= 0:
            self.__shot_delay = constants.SHOT_DELAY
            velocity = pygame.Vector2(0, 1).rotate(self.__rotation)
            Shot(self.position.x, self.position.y, velocity)

    def rotate(self, dt):
        self.__rotation += constants.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.__rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.__shot_delay -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

        pygame.draw.circle(
            screen,
            color=(255, 0, 0),
            center=self.position,
            radius=self.radius,
            width=2,
        )


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, constants.SHOT_RADIUS)
        self.velocity = direction * constants.SHOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color=(255, 255, 255),
            center=self.position,
            radius=self.radius,
            width=2,  # TODO: replace this with a constant
        )

    def update(self, dt):
        self.position += self.velocity * dt
