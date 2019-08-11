import pygame

class Ship():

    def __init__(self, init_settings, screen):
        """ Initializa ship and starting position """
        self.screen = screen
        self.init_settings = init_settings

        self.image = pygame.image.load('media/img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal value for ship's center
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.init_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.init_settings.ship_speed_factor

        # update rect form self.center
        self.rect.centerx = self.center

    def blitme(self):
        """ draw ship """
        self.screen.blit(self.image, self.rect)