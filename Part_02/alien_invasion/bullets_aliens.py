import pygame
from pygame.sprite import Sprite

class Bullets_aliens(Sprite):

    def __init__(self, ai_settings, superficie, alien):
        super().__init__()
        self.ai_settings = ai_settings
        self.superficie = superficie

        self.image = pygame.image.load("images/laserGreen11.png").convert()
        self.image_transform = pygame.transform.scale(self.image, (ai_settings.bullet_largura, ai_settings.bullet_altura))
        self.rect = self.image_transform.get_rect()
        self.superficie_rect = superficie.get_rect()

        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.y = float(self.rect.y)

    def update(self):
        self.y = self.y + self.ai_settings.bullet_aliens_speed_factor
        self.rect.y = self.y


    def draw_bullet(self):
        self.superficie.blit(self.image_transform, self.rect)

