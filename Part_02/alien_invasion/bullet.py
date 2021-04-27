import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """"Uma classe que administra projéteis disparados pela espaçonave"""

    def __init__(self, ai_settings, superficie, espaconave):
        """"Cria um objeto para o projétil na posição atual da espaçonave."""
        super().__init__()
        self.superficie = superficie
        self.ai_settings = ai_settings

        #Cria uma imagem bullet e coloca ela no formato de um retângulo
        self.image = pygame.image.load("images/laserRed16.png").convert()
        self.image_transform = pygame.transform.scale(self.image, (ai_settings.bullet_largura, ai_settings.bullet_altura))
        self.image_transform.set_colorkey(0)
        self.rect = self.image_transform.get_rect()
        #Eixo x - Retângulo do projétil é igual ao retangulo da imagem espaçonave
        self.rect.centerx = espaconave.rect.centerx
        self.rect.top = espaconave.rect.top

        #Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """"Move o projétil para cima na tela."""
        # Atualiza a posição decimal do projétil
        self.y = self.y - self.speed_factor
        # Atualiza a posição do retângulo
        self.rect.y = self.y


    def desenha_bala(self):
        """"Desenha o projétil na tela."""
        self.superficie.blit(self.image_transform, self.rect)