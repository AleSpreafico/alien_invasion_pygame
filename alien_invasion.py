import sys

import pygame

from settings import Settings
from ship import Ship


def run_game():
    """ Initializing Game and Screen """
    pygame.init()
    init_settings = Settings()

    screen = pygame.display.set_mode(
        (init_settings.screen_width, init_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)

    """ Start Game """
    while True:
        """ listening mouse and key events """
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(init_settings.bg_color)
        ship.blitme()

        pygame.display.flip()


run_game()
