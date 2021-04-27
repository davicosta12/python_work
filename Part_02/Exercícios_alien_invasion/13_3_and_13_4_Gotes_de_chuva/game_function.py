import sys
import pygame
from gota import Gota


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()


def Apaga_gotas(gotas, settings):
    for gota in gotas.copy():
        if gota.rect.top >= settings.screen_height:
            gotas.remove(gota)
    print(len(gotas))


def fleet_created(settings, screen, gotas):
    gota = Gota(screen, settings)
    avaliando_space_x =  settings.screen_width - gota.rect.width
    avaliando_space_y = settings.screen_height + 2 * gota.rect.height
    number_gotas = int(avaliando_space_x / (2 * gota.rect.width))
    number_linhas = int(avaliando_space_y / (2 * gota.rect.height))

    for number_linha in range(number_linhas):
        for number_gota in range(number_gotas):
            gota = Gota(screen, settings)
            position_x = gota.rect.width + (2 * gota.rect.width) * number_gota
            gota.y = 2 * gota.rect.height * number_linha
            gota.rect.y = gota.y
            gota.rect.x = position_x
            gotas.add(gota)


def cria_linha_gota(screen, settings, gotas):
    for gota in gotas.sprites():
        if gota.VerificaOndeAgotaEncosta():
            gota = Gota(screen, settings)
            avaliando_space_x = settings.screen_width - gota.rect.width
            number_gotas = int(avaliando_space_x / (2 * gota.rect.width))

            for number_gota in range(number_gotas):
                gota = Gota(screen, settings)
                position_x = gota.rect.width + (2 * gota.rect.width) * number_gota
                gota.rect.x = position_x
                gotas.add(gota)
            break


def screen_update(screen, bg_color, gotas):
    screen.fill(bg_color)
    gotas.draw(screen)
    pygame.display.flip()


def update_gotas(settings, screen, gotas):
    cria_linha_gota(screen, settings, gotas)
    Apaga_gotas(gotas, settings)
    gotas.update()

