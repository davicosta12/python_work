import pygame

class Basket_man():

    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/basket_man.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x = self.x + self.ai_settings.basket_man_speed_factor
            self.rect.x = self.x
        if self.moving_left and self.rect.left > 0:
            self.x = self.x - self.ai_settings.basket_man_speed_factor
            self.rect.x = self.x


    def blit_me(self):
        self.screen.blit(self.image, self.rect)


    def center_basket_man(self):
        self.x = self.screen_rect.centerx
        self.rect.x = self.x