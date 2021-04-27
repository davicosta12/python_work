import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Criando retângulo
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.screen_rect = screen.get_rect()

        # Definir a posição dos retângulos criados na tela
        self.rect.centery = ship.rect.centery
        self.rect.left = ship.rect.right


        # Cor da bala
        self.color = self.ai_settings.bullet_color

        # Posição inicial da bala
        self.x = float(self.rect.x)


    def update(self):
        self.x = self.x + self.ai_settings.bullet_speed_factor
        self.rect.x = self.x


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
