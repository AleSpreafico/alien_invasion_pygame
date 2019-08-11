import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage bullets fired from ship"""
    def __init__(self, init_settings, screen, ship):
        super().__init__()
        self.init_settings = init_settings
        self.screen = screen

        # Create bullet
        self.rect = pygame.Rect(0,0, init_settings.bullet_width, init_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = init_settings.bullet_color
        self.speed_factor = init_settings.bullet_speed_factor

    def update(self):
        """ Move the bullet up the screen """
        # Update decimal position
        self.y -= self.speed_factor

        # Update rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """ draw bullet on screen """
        pygame.draw.rect(self.screen, self.color, self.rect)