import pygame
from pygame.sprite import Sprite
from random import randint

class Torpedo(Sprite):

    def __init__(self, ai_settings, superficie, special_ship):
        super().__init__()
        self.ai_settings = ai_settings
        self.superficie = superficie
        self.special_ship = special_ship

        self.image = pygame.image.load("images/torpedo.bmp")
        self.rect = self.image.get_rect()
        self.superficie_rect = superficie.get_rect()

        self.rect.x = randint(self.superficie_rect.left, self.superficie_rect.right - 46)
        self.rect.top = self.special_ship.rect.bottom

        self.y = float(self.rect.y)


    def update(self):
        if not self.ai_settings.active:
            self.y = self.y + self.ai_settings.torpedo_speed_factor
            self.rect.y = self.y



    def draw_me(self):
        self.superficie.blit(self.image, self.rect)




