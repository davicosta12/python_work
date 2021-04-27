import pygame
from pygame.sprite import Sprite

class Gota(Sprite):

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('image/gota.bmp')
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.bottom = self.screen_rect.top

        self.y = float(self.rect.y)


    def VerificaOndeAgotaEncosta(self):
        if self.rect.top == self.settings.screen_height:
            return True


    def update(self):
        self.y = self.y + self.settings.gota_speed_factor
        self.rect.y = self.y


    def blit_me(self):
        self.screen.blit(self.image, self.rect)
