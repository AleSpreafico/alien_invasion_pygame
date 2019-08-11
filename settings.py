
class Settings:
    """ Settings """

    def __init__(self):
        """ Init settings """

        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship
        self.ship_speed_factor = 1.5

        # Bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
