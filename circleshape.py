import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers: list[pygame.sprite.Group]

    def __init__(self, x, y, radius):
        super().__init__(self.containers)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
