import enum

import pygame


class GameState(enum.Enum):
    RUNNING = 0
    STOP = 1


class GameMonitor(pygame.sprite.Sprite):
    containers: list[pygame.sprite.Group]
    gamestate: GameState = GameState.RUNNING

    def __init__(self, color: tuple[int, int, int]):
        super().__init__(self.containers)

        self.__color = color

    def draw(self, screen):
        screen.fill(self.__color)

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameMonitor.gamestate = GameState.STOP

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            GameMonitor.gamestate = GameState.STOP
