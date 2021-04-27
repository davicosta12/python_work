import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        self.image = pygame.image.load('images/foguete.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center
        self.rect.left = self.screen_rect.left

        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False


    def update(self):
        if self.moving_up and self.rect.top >= 0:
            self.y = self.y - self.ai_settings.ship_speed_factor
            self.rect.y = self.y
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom :
            self.y = self.y + self.ai_settings.ship_speed_factor
            self.rect.y = self.y

    def blit_me(self):
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        self.y = self.screen_rect.centery
        self.rect.y = self.y
