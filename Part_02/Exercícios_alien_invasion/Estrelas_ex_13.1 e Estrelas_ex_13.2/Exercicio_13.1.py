import pygame

from settings import Settings
import game_fuction13_1 as gf

from pygame.sprite import Group

def inicia_jogo():
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    back_ground_color = settings.back_ground_color
    pygame.display.set_caption('Estrelas')

    estrelas = Group()
    gf.Cria_frota(settings, screen, estrelas)

    while True:
        gf.eventos_teclas()
        gf.Atualiza_a_screen(screen, back_ground_color, estrelas)

inicia_jogo()