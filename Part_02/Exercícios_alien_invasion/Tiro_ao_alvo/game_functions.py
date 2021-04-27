import sys
import pygame
from bullets import Bullets
from time import sleep

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False

def check_keydown_events(event, screen, ai_settings, stats, ship, bullets, alvo):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(bullets, alvo, ship, stats)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE and stats.game_active:
        if len(bullets) < ai_settings.bullet_limited:
            bullet = Bullets(ai_settings, screen, ship)
            bullets.add(bullet)

def start_game(bullets, alvo, ship, stats):
    pygame.mouse.set_visible(False)
    stats.game_active = True
    stats.game_reset()
    bullets.empty()
    ship.center_ship()
    alvo.center_alvo()


def check_events_mouse(ai_settings, button, stats, alvo, ship, bullets):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    button_clicked = button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.inicializa_config()
        start_game(bullets, alvo, ship, stats)


def check_events(screen, ai_settings, stats,  ship, bullets, button, alvo):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ai_settings, stats, ship, bullets, alvo)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_events_mouse(ai_settings, button, stats, alvo, ship, bullets)


def update_ship(ship):
    ship.update()


def Verifica_a_quantidade_de_chances(ai_settings, stats, bullets, ship, alvo):
    if stats.bullet_limit > 0:
        ai_settings.inicializa_com_a_direction_correta()
        stats.bullet_limit = stats.bullet_limit - 1
        bullets.empty()
        ship.center_ship()
        alvo.center_alvo()
        sleep(0.5)
    else:
        bullets.empty()
        ship.center_ship()
        alvo.center_alvo()
        pygame.mouse.set_visible(True)
        stats.game_active = False


def remove_bullets_edge(ai_settings, bullets, stats, ship, alvo):
    for bullet in bullets.copy():
        if bullet.rect.left >= bullet.screen_rect.right:
            bullets.remove(bullet)
            Verifica_a_quantidade_de_chances(ai_settings, stats, bullets, ship, alvo)
        print(len(bullets))

def check_bullet_hit(ai_settings, bullets, alvo):
    if pygame.sprite.spritecollideany(alvo, bullets):
        ai_settings.incrementa_novas_configs()

    pygame.sprite.spritecollide(alvo, bullets, True)


def update_bullets(ai_settings, bullets, stats, ship, alvo):
    bullets.update()
    remove_bullets_edge(ai_settings, bullets, stats, ship, alvo)
    check_bullet_hit(ai_settings, bullets, alvo)


def update_alvo(ai_settings, alvo):
    alvo.update()
    if alvo.check_alvo_edge():
        ai_settings.alvo_direction = ai_settings.alvo_direction * -1


def screen_update(screen, stats, bg_color, alvo, ship, bullets, button):
    screen.fill(bg_color)

    ship.blit_me()

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    alvo.draw_rect()

    if not stats.game_active:
        button.draw_button()

    pygame.display.flip()

