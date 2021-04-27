import pygame

class Alvo():

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen

        # Cria uma retângulo
        self.rect = pygame.Rect(0, 0, ai_settings.alvo_width, ai_settings.alvo_height)
        self.screen_rect = screen.get_rect()

        # Direciona o retângulo na tela
        self.rect.center = self.screen_rect.center
        self.rect.right = self.screen_rect.right

        # Define a cor do retângulo
        self.color = ai_settings.alvo_color

        # Posição inicial
        self.y = float(self.rect.y)


    def check_alvo_edge(self):
        if self.rect.top <= self.screen_rect.top:
            return True
        if self.rect.bottom >= self.screen_rect.bottom:
            return True


    def update(self):
        self.y = (self.y - self.ai_settings.alvo_speed_factor
                            * self.ai_settings.alvo_direction)
        self.rect.y = self.y


    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


    def center_alvo(self):
        self.y = self.screen_rect.centery
        self.rect.y = self.y
