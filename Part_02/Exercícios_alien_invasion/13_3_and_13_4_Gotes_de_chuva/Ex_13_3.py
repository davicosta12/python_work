import pygame

import game_function as gf
from settings import Settings
from pygame.sprite import Group

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    bg_color = (settings.bg_color)
    pygame.display.set_caption('Chuva')

    # Criando um grupo de gotas
    gotas = Group()

    # Cria frota
    gf.fleet_created(settings, screen, gotas)

    while True:
        gf.check_event()
        gf.update_gotas(gotas)
        gf.screen_update(screen, bg_color, gotas)


run_game()