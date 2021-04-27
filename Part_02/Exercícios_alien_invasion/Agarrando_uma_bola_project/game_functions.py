import sys
import pygame
from time import sleep

from basket_boll import Basket_boll


def check_event(basket_man):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_RIGHT:
                basket_man.moving_right = True
            elif event.key == pygame.K_LEFT:
                basket_man.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                basket_man.moving_right = False
            elif event.key == pygame.K_LEFT:
                basket_man.moving_left = False


def Cria_bola(screen, ai_settings, basket_boll_group, stats):
    if len(basket_boll_group) == 0 and stats.game_active:
        new_basket_boll = Basket_boll(screen, ai_settings)
        basket_boll_group.add(new_basket_boll)


def apaga_bola_aresta_inferior(ai_settings, basket_boll_group, basket_man, stats):
    for basket_boll in basket_boll_group.copy():
        if basket_boll.rect.top >= ai_settings.screen_height:
            basket_boll_group.remove(basket_boll)
            basketBoll_falldown(basket_man, basket_boll_group, stats)
    print(len(basket_boll_group))


def basketBoll_falldown(basket_man, basket_boll_group, stats):
    if stats.basket_boll_bottom > 0:
        stats.basket_boll_bottom = stats.basket_boll_bottom - 1

        basket_boll_group.empty()

        basket_man.center_basket_man()

        sleep(0.5)

    else:
        stats.game_active = False


def basket_boll_update(basket_boll_group, ai_settings, screen, basket_man, stats):
    basket_boll_group.update()

    pygame.sprite.spritecollide(basket_man, basket_boll_group, True)

    apaga_bola_aresta_inferior(ai_settings, basket_boll_group, basket_man, stats)

    Cria_bola(screen, ai_settings, basket_boll_group, stats)


def update_screen(screen, bg_color, basket_man, basket_boll_group):
    screen.fill(bg_color)
    basket_man.blit_me()
    basket_boll_group.draw(screen)
    pygame.display.flip()