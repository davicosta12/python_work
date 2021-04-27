import sys
import pygame
from estrela import Estrela

def eventos_teclas():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def Atualiza_a_screen(screen, back_ground_color, estrelas):
    screen.fill(back_ground_color)
    estrelas.draw(screen)
    pygame.display.flip()


def Obtem_numero_linhas(settings, estrela):
    avaliando_space_y = settings.screen_height - estrela.rect.height
    number_linhas = int(avaliando_space_y / (2 * estrela.rect.height))
    return number_linhas


def Obtem_numero_estrelas(settings, estrela):
    avaliando_space_x = settings.screen_width - estrela.rect.width
    numero_estrelas_x = int(avaliando_space_x / (2 * estrela.rect.width))
    return numero_estrelas_x


def Cria_estrelas(screen, settings, estrelas, number_estrela, number_linha):
    estrela = Estrela(screen, settings)
    estrela.position_x = estrela.rect.width + 2 * estrela.rect.width * number_estrela
    estrela.postion_y = estrela.rect.height + 2 * estrela.rect.height * number_linha
    estrela.rect.x = estrela.position_x
    estrela.rect.y = estrela.postion_y
    estrelas.add(estrela)


def Cria_frota(settings, screen, estrelas):
    estrela = Estrela(screen, settings)
    numero_estrelas_x = Obtem_numero_estrelas(settings, estrela)
    number_linhas = Obtem_numero_linhas(settings, estrela)

    for number_linha in range(number_linhas):
        for number_estrela in range(numero_estrelas_x):
            Cria_estrelas(screen, settings, estrelas, number_estrela, number_linha)