import pygame
from os import path
from pygame.sprite import Sprite

class Especial_ship_left(Sprite):

    def __init__(self, ai_settings, superficie, sb):
        super().__init__()
        self.ai_settings = ai_settings
        self.superficie = superficie
        self.scoreboard = sb

        specialShip_dir = path.join(path.dirname(__file__), 'images')
        tipo_special_ship = 'special_ship00.bmp'
        self.image = pygame.image.load(path.join(specialShip_dir, tipo_special_ship))

        self.rect = self.image.get_rect()
        self.superficie_rect =  superficie.get_rect()

        self.rect.right = self.superficie_rect.left
        self.rect.top = self.scoreboard.level_rect.bottom

        self.x = float(self.rect.x)


    def update(self):
        self.x = self.x + self.ai_settings.especial_ship_speed_factor
        self.rect.x = self.x


    def blit_me(self):
        self.superficie.blit(self.image, self.rect)