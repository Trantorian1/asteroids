import pygame

import monitor
import player
from constants import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    monitor.GameMonitor.containers = [updatable, drawable]
    monitor.GameMonitor((0, 0, 0))

    player.Player.containers = [updatable, drawable]
    player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while monitor.GameMonitor.gamestate == monitor.GameState.RUNNING:
        # Game updates
        for entity in updatable:
            entity.update(dt)

        # Draw to screen
        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
