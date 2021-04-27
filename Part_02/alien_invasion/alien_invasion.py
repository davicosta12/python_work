import pygame
from pygame.sprite import Group

from random import choice
from music import Music
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import EspacoNave
from bullets_aliens import Bullets_aliens
from alien import Alien
import game_function as gf

def comeca_jogo():
	# Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	superficie = pygame.display.set_mode(
		(ai_settings.superficie_largura, ai_settings.superficie_altura))
	pygame.display.set_caption("Alien Invasion")

	# Cria o botão Play
	play_button = Button(ai_settings, superficie, "Play")
	
	# Cria uma espaçonave
	espaconave = EspacoNave(ai_settings, superficie)

	# Cria alien
	alien = Alien(ai_settings, superficie)
	bullet_aliens_ins = Bullets_aliens(ai_settings, superficie, alien)

	# Flag que determina quando a espaçonave deve ser desenhada
	flag_draw_ship = False

	#Cria os grupos
	bullets = Group()
	bullet_aliens = Group()
	explosion = Group()
	aliens = Group()
	special_ship = Group()
	torpedo = Group()
	barreiras = Group()

	# Cria barreiras do game
	gf.criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien)

	#Cria a frota de alienígenas
	gf.cria_frota(ai_settings, superficie, aliens, espaconave)

	#Cria uma instância para armazenar dados estatísticos do jogo
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, superficie, stats)

	# Sons do jogo
	#Cria uma instância da classe Music
	music_game = Music(ai_settings)

	# Cria três sons de explosões alienígenas
	explosion_sound = music_game.sound_list_explosions()

	# Cria lista de imagens diferenciadas de explosões
	explosion_anim = gf.armazena_na_list_imagens_explosoes()

	# Inicia a música de introdução do jogo
	music_game.music_intro()

	# Inicia o laço principal do jogo
	while True:
		gf.check_events(ai_settings, superficie, stats, sb, play_button, espaconave,
						aliens, bullets, bullet_aliens, music_game, special_ship,
					   torpedo, barreiras, alien)

		if stats.game_active:
			espaconave.update()

			gf.update_bullets(ai_settings, stats, sb, superficie, bullets,
				 bullet_aliens, aliens, espaconave, special_ship, explosion,
							  explosion_anim, explosion_sound, torpedo, barreiras, alien)


			gf.update_special_ship(ai_settings, superficie, special_ship, sb, alien)



			gf.update_torpedo(ai_settings, stats, sb, superficie, espaconave, aliens,
							  bullets, bullet_aliens, music_game, explosion, explosion_anim, play_button, special_ship,
							  torpedo, barreiras)


			gf.update_aliens(ai_settings, stats, sb, superficie, espaconave, aliens, bullets,
							 bullet_aliens, music_game, explosion,
							 explosion_anim, play_button, special_ship, torpedo, barreiras)


			gf.update_bullets_aliens(ai_settings, superficie,
					espaconave, explosion_anim, explosion, bullet_aliens,stats, sb, aliens, bullets, music_game,
									 play_button, special_ship, torpedo, barreiras)


			explosion.update()


		gf.update_screen(ai_settings, superficie, espaconave, aliens, bullets, stats, sb, play_button,
				  	bullet_aliens, explosion, special_ship, torpedo, barreiras, flag_draw_ship)


comeca_jogo()