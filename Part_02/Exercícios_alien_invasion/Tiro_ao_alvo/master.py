import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from Objeto import Alvo
from game_stats import Stats
from button import Button
import game_functions as gf

def run_game():
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Tiro ao alvo')
    bg_color = ai_settings.bg_color

    button = Button(ai_settings, screen, "Play")

    ship = Ship(ai_settings, screen)
    bullets = Group()
    stats = Stats(ai_settings)
    alvo = Alvo(ai_settings, screen)

    while True:
        gf.check_events(screen, ai_settings, stats, ship, bullets, button, alvo)
        if stats.game_active:
            gf.update_ship(ship)
            gf.update_bullets(ai_settings, bullets, stats, ship, alvo)
            gf.update_alvo(ai_settings, alvo)
        gf.screen_update(screen, stats, bg_color, alvo, ship, bullets, button)

run_game()

