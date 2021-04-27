import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):

    def __init__(self, explosion_anim, superficie, center, size):
        super().__init__()
        self.superficie = superficie
        self.explosion_anim = explosion_anim
        self.size = size

        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frama_rate = 10


    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frama_rate:
            self.last_update = now
            self.frame = self.frame + 1
            if self.frame == len(self.explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


    def draw_explosion(self):
        self.superficie.blit(self.image, self.rect)






