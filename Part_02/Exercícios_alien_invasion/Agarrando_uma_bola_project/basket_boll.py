import pygame
from random import randint
from pygame.sprite import Sprite


class Basket_boll(Sprite):

    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/bola_basket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.y = self.screen_rect.y
        self.rect.x = randint(self.screen_rect.left, self.screen_rect.right - 46)

        self.y = float(self.rect.y)


    def update(self):
        self.y = self.y + self.ai_settings.basket_boll_speed_factor
        self.rect.y = self.y


    def blit_me(self):
        self.screen.blit(self.image, self.rect)