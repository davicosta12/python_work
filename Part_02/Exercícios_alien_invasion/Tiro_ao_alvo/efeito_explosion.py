import pygame

class Explosion():

    def __init__(self, bullet, screen):
        self.screen = screen
        self.bullet = bullet

        self.image = pygame.image.load('images/efeito_explossão.bmp')
        self.rect = self.image.get_rect()

        self.rect.centery = bullet.rect.centery
        self.rect.right = bullet.rect.left


    def Verifica_edge_boolena(self):
        if self.bullet.rect.left >= self.bullet.screen_rect.right:
            return True


    def blit_me(self):
        self.screen.blit(self.image, self.rect)
