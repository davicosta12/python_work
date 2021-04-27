import pygame
from pygame.sprite import Sprite

class Estrela(Sprite):

    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('imagens/estrela.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.position_x = float(self.rect.x)
        self.postion_y = float(self.rect.y)

    def DesenhaEstrela(self):
      self.screen.blit(self.image, self.rect)
