import pygame
from pygame.sprite import Sprite

class Square(Sprite):

    def __init__(self,  ai_settings, superficie, espaconave):
        super().__init__()
        self.ai_settings =  ai_settings
        self.superficie = superficie

        self.rect = pygame.Rect(0, 0, ai_settings.bullet_largura, ai_settings.bullet_largura)
        self.superficie_rect = superficie.get_rect()
        self.rect.left = self.rect.width * 6
        self.rect.bottom = espaconave.rect.top - 8 * self.rect.bottom

        self.square_color = (0, 160, 0)


    def blit_rect(self):
        pygame.draw.rect(self.superficie, self.square_color, self.rect)
