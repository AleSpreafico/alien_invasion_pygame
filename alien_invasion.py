import sys

import pygame
from pygame.sprite import Group
import helpers as h

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

    ship = Ship(init_settings, screen)

    bullets = Group()

    """ Start Game """
    while True:
        """ listening mouse and key events """
        h.check_events(init_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        h.update_screen(init_settings, screen, ship, bullets)


run_game()
