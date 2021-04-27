import pygame
from pygame.sprite import Group
import game_functions as gf

from basket_man import Basket_man
from basket_boll import Basket_boll
from settings import Settings
from game_stats import GameStats


def run_game():
    pygame.init()
    ai_settings =  Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    bg_color = (ai_settings.screen_color)
    pygame.display.set_caption('BASQUETE GAME')

    basket_man = Basket_man(screen, ai_settings)

    basket_boll = Basket_boll(screen, ai_settings)

    basket_boll_group = Group()
    basket_boll_group.add(basket_boll)

    stats = GameStats(ai_settings)


    while True:
        gf.check_event(basket_man)

        if stats.game_active:
            basket_man.update()
            gf.basket_boll_update(basket_boll_group, ai_settings, screen, basket_man, stats)

        gf.update_screen(screen, bg_color, basket_man, basket_boll_group)



run_game()