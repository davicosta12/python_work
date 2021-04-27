import pygame
from random import choice
from os import path
from pygame.sprite import Sprite

class Alien(Sprite):
    """"Uma classe que representa um único alienígena da frota."""

    def __init__(self, ai_settings, superficie):
        """"Inicializa o alienígene e define sua posição inicial."""
        super().__init__()
        self.superficie = superficie
        self.ai_settings = ai_settings

        # Carrega a imagem do alienígena e define seu atributo rect
        enemy_dir = path.join(path.dirname(__file__), 'images')
        tipo_enemy = 'enemy00.bmp'
        self.image = pygame.image.load(path.join(enemy_dir, tipo_enemy))
        self.rect = self.image.get_rect()

        # Inicia cada novo alienigena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Armazina a posição exata do alienígena
        self.x = float(self.rect.x)


    def check_edges(self):
        """"Devolve True se o alienígena estiver na borda da tela."""
        superficie_rect = self.superficie.get_rect()
        if self.rect.right >= superficie_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def update(self):
        """"Move o alienígena para a direita."""
        self.x = self.x + (self.ai_settings.alien_speed_factor *
                                self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def blitme(self):
        """"Desenha o alienígena em sua posição atual."""
        self.superficie.blit(self.image, self.rect)


    def retorna_cores(self):
        if self.tipo_enemy == 'enemy00.bmp':
            return 'special_ship00.bmp'
        elif self.tipo_enemy == 'enemy01.bmp':
            return 'special_ship01.bmp'