import sys
from time import sleep
import random
import pygame

from bullets_aliens import Bullets_aliens
from explosion import Explosion
from bullet import Bullet
from torpedo import Torpedo
from alien import Alien
from especial_ship import Especial_ship
from especial_ship_left import Especial_ship_left
from square import Square


def fire_bullet(ai_settings, stats, superficie,  espaconave, bullets):
	# Cria um novo projétil e o adiciona ao grupo de projéteis
	if len(bullets) < ai_settings.bullets_permitidas and stats.game_active:
		now = pygame.time.get_ticks()
		if now - ai_settings.bullet_last_shot > ai_settings.bullet_shoot_delay:
			ai_settings.bullet_last_shot = now
			new_bullet = Bullet(ai_settings, superficie, espaconave)
			bullets.add(new_bullet)
			ai_settings.shoot_sound.play()


def check_keydow_event(event, ai_settings, stats, sb, aliens,
					   superficie, espaconave, bullets, bullet_aliens, music_game, barreiras, alien):
	"""Responde a pressionamentos de telca."""
	if event.key == pygame.K_RIGHT:
		espaconave.moving_right = True
	elif event.key == pygame.K_LEFT:
		espaconave.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings, stats, superficie, espaconave, bullets)
	elif event.key == pygame.K_q:
		write_high_score(stats, sb)
		sys.exit()
	elif event.key == pygame.K_p and not stats.game_active:
		start_game(ai_settings, superficie, stats, sb, aliens, bullets,
				   bullet_aliens, espaconave, music_game, barreiras, alien)


def check_keyup_event(event, espaconave):
	"""Responde a solturas de tecla."""
	if event.key == pygame.K_RIGHT:
		espaconave.moving_right = False
	elif event.key == pygame.K_LEFT:
		espaconave.moving_left = False


def check_events(ai_settings, superficie, stats, sb, play_button,
				 espaconave, aliens, bullets, bullet_aliens,
				 music_game, special_ship, torpedo, barreiras, alien):
	"""Responde a eventos de pressionamento de teclas e de mouse."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			write_high_score(stats, sb)
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydow_event(event, ai_settings, stats, sb, aliens, superficie,
							   espaconave, bullets, bullet_aliens, music_game, barreiras, alien)
		elif event.type == pygame.KEYUP:
			check_keyup_event(event, espaconave)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(ai_settings, superficie, stats, sb, play_button, espaconave, aliens,
					  bullets, bullet_aliens, music_game,
							  special_ship, torpedo, barreiras, alien, mouse_x, mouse_y)


def start_game(ai_settings, superficie, stats, sb, aliens, bullets, bullet_aliens,
			   espaconave, music_game, special_ship, torpedo, barreiras, alien):
	# Oculta o cursor do mouse
	pygame.mouse.set_visible(False)

	# Reinicia os dados estatísticos do jogo
	stats.reset_stats()
	stats.game_active = True
	# Para a música atual
	music_game.stop_music()
	# Carrega a próxima música
	music_game.music_gameplay()

	# Reinicia as imagens do painel de pontuação
	sb.prep_images()

	# Esvazia a lista de alienígenas e de projéteis
	special_ship.empty()
	torpedo.empty()
	aliens.empty()
	bullets.empty()
	bullet_aliens.empty()


	# Cria uma nova frota e centraliza a espaçonave
	criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien)
	cria_frota(ai_settings, superficie, aliens, espaconave)
	espaconave.center_espaconave()


def check_play_button(ai_settings, superficie, stats, sb, play_button, espaconave, aliens,
					  bullets, bullet_aliens, music_game, special_ship,
					  torpedo, barreiras, alien, mouse_x, mouse_y):
	""""Inicia um novo jogo quando o jogador clicar em Play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		ai_settings.initialize_dynamic_settings()
		start_game(ai_settings, superficie, stats, sb, aliens, bullets, bullet_aliens,
				   espaconave, music_game, special_ship, torpedo, barreiras, alien)


def update_screen(ai_settings, superficie, espaconave, aliens, bullets, stats, sb, play_button,
				  bullet_aliens, explosion, special_ship, torpedo, barreiras, flag_draw_ship):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	# Redesenha a tela a cada passagem pelo laço
	superficie.fill(ai_settings.bg_color)
	superficie.blit(ai_settings.back_ground_image, ai_settings.back_ground_rect)

	# Redesenha todos os projéteis atrás da espaçonave e dos alienígenas
	for bullet in bullets.sprites():
		if stats.game_active:
			bullet.desenha_bala()

	for bullet in bullet_aliens.sprites():
		if stats.game_active:
			bullet.draw_bullet()

	for sprite in special_ship.sprites():
		if stats.game_active:
			sprite.blit_me()

	for sprite in torpedo.sprites():
		if stats.game_active and not ai_settings.active:
			sprite.draw_me()

	#Desenha espaçonave
	if not flag_draw_ship and stats.game_active:
		espaconave.blitme()

	if stats.game_active:
		aliens.draw(superficie)

	if stats.game_active:
		for square in barreiras.sprites():
			square.blit_rect()

	explosion.draw(superficie)

	# Desenha a informação sobre pontuação
	sb.show_score()

	# Desenha o botão Play se o jogo estiver inativo
	if not stats.game_active:
		play_button.draw_button()
	
	# Deixa a tela mais recente visível
	pygame.display.flip()


def created_explosion_player(ai_settings, explosion_anim, superficie, espaconave, explosion):
	death_explosion = Explosion(explosion_anim, superficie, espaconave.rect.center, 'ship')
	death_explosion.frama_rate = 70
	explosion.add(death_explosion)
	ai_settings.player_explosion.play()
	return death_explosion


def Cria_looping_de_imagem_explosao(ai_settings, superficie, espaconave, aliens, bullets, stats, sb, play_button,
					  bullet_aliens, explosion, death_explosion, special_ship, torpedo, barreiras):
	while death_explosion.alive():
		superficie.fill(ai_settings.bg_color)

		update_screen(ai_settings, superficie, espaconave, aliens, bullets, stats, sb, play_button,
					  bullet_aliens, explosion, special_ship, torpedo, barreiras, flag_draw_ship = True)
		explosion.update()
		pygame.display.flip()

def diversos_fatores_aplicados_ship_hit(stats, sb, aliens, bullets,
					bullet_aliens, ai_settings, superficie, espaconave, special_ship, torpedo):

	ai_settings.active = True
	# Decrementa espaconave_left
	stats.espaconave_left = stats.espaconave_left - 1

	# Atualiza o painel de pontuação
	sb.prep_ships()

	# Esvazia a lista de alienígenas e de projéteis
	special_ship.empty()
	torpedo.empty()
	aliens.empty()
	bullets.empty()
	bullet_aliens.empty()

	# reinicia os tempos

	# espacionave especial
	ai_settings.last_update_ship = pygame.time.get_ticks()


	# torpedo
	ai_settings.last_update_torpedo = pygame.time.get_ticks()

	# disparos alienígenas
	ai_settings.last_update = pygame.time.get_ticks()


	# Cria uma nova frota e centraliza a espaçonave
	cria_frota(ai_settings, superficie, aliens, espaconave)
	espaconave.center_espaconave()

	# Aumenta a música novamente
	pygame.mixer.music.set_volume(0.4)


def check_bullet_ship_collision(ai_settings, superficie,
	espaconave, explosion_anim, explosion, bullet_aliens,
			stats, sb, aliens, bullets, music_game, play_button, special_ship, torpedo, barreiras):

	colissions = pygame.sprite.spritecollide(espaconave, bullet_aliens, True)

	if colissions:
		espaconave_hit(ai_settings, stats, sb, superficie, espaconave, aliens,
					   bullets, bullet_aliens, music_game, explosion, explosion_anim, play_button, special_ship,
					   torpedo, barreiras)


def removendo_bullet_na_parteInferior(bullet_aliens):
	for bullet_alien in bullet_aliens.copy():
		if bullet_alien.rect.top >= bullet_alien.superficie_rect.bottom:
			bullet_aliens.remove(bullet_alien)


def bullet_aleatoria_dos_aliens(ai_settings, superficie, aliens, bullet_aliens):
	lista_aliens = aliens.sprites()
	alien = random.choice(lista_aliens)
	bullet_postion = Bullets_aliens(ai_settings, superficie, alien)
	bullet_aliens.add(bullet_postion)


def created_bullet_alien(ai_settings, superficie, aliens, bullet_aliens):
	now = pygame.time.get_ticks()
	if now - ai_settings.last_update > ai_settings.time_seconds:
		ai_settings.last_update = now
		bullet_aleatoria_dos_aliens(ai_settings, superficie, aliens, bullet_aliens)
		ai_settings.shoot_sound_alien.play()
		removendo_bullet_na_parteInferior(bullet_aliens)


def check_bullet_barreiras(bullet_aliens, barreiras):
	collision = pygame.sprite.groupcollide(bullet_aliens, barreiras, True, True)


def update_bullets_aliens(ai_settings, superficie,
	espaconave, explosion_anim, explosion,
		bullet_aliens, stats, sb, aliens, bullets, music_game, play_button, especial_ship, torpedo, barreiras):

	created_bullet_alien(ai_settings, superficie, aliens, bullet_aliens)
	bullet_aliens.update()

	check_bullet_ship_collision(ai_settings, superficie,
		espaconave, explosion_anim, explosion, bullet_aliens,
		stats, sb, aliens, bullets, music_game, play_button, especial_ship, torpedo, barreiras)

	check_bullet_barreiras(bullet_aliens, barreiras)


def remove_bullets(bullets):
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def update_bullets(ai_settings, stats, sb, superficie, bullets, bullet_aliens, aliens, espaconave, special_ship, explosion,
				   explosion_anim, explosion_sound, torpedo, barreiras, alien):
	""""Atualiza a posição dos projéteis e se livra dos projéteis antigos."""
	# Atualiza as posições dos projéteis
	bullets.update()

	# Livra-se dos projéteis que desapareceram
	remove_bullets(bullets)
	check_bullets_collisions(bullets, bullet_aliens, explosion_anim, explosion, explosion_sound, superficie)
	check_bullet_alien_collision(ai_settings, stats, sb, superficie, bullets, aliens, espaconave,
								 explosion, explosion_anim, explosion_sound, barreiras, alien)
	check_bullet_special_ship_collision(ai_settings, stats, sb, superficie, bullets, aliens, espaconave, special_ship,
								 explosion, explosion_anim, explosion_sound, torpedo)
	check_bullet_torpedo(ai_settings, explosion_anim, explosion, superficie, torpedo, bullets)
	check_bullet_barreira(barreiras, bullets)


def write_high_score(stats, sb):
	"""Faz a leitura da high score atual e grava em um outro arquivo"""
	high_score = check_high_score(stats, sb)

	with open("write_high_score.txt", "w") as obj_factor:
		obj_factor.write(str(high_score))


def check_bullet_barreira(barreiras, bullets):
	collision = pygame.sprite.groupcollide(bullets, barreiras, True, True)


def check_bullet_torpedo(ai_settings, explosion_anim, explosion, superficie, torpedo, bullets):
	if ai_settings.active == False:
		collision_torp = pygame.sprite.groupcollide(bullets, torpedo, True, True)
		if collision_torp:
			for hit in collision_torp:
				explod = Explosion(explosion_anim, superficie, hit.rect.center, 'torpedo')
				sound = ai_settings.player_explosion
				sound.play()
				explod.frama_rate = 50
				explosion.add(explod)

			ai_settings.active = True


def check_bullets_collisions(bullets, bullet_aliens, explosion_anim, explosion, explosion_sound, superficie):
	collision_bullets = pygame.sprite.groupcollide(bullets, bullet_aliens, True, True)

	if collision_bullets:
		for hit in collision_bullets:
			expl = Explosion(explosion_anim, superficie, hit.rect.center, 'alien')
			explosion.add(expl)
			sound = random.choice(explosion_sound)
			sound.play()


def check_bullet_special_ship_collision(ai_settings, stats, sb, superficie, bullets, aliens, espaconave, special_ship,
								 explosion, explosion_anim, explosion_sound, torpedo):
	collision = pygame.sprite.groupcollide(bullets, special_ship, True, True)

	if collision:
		for hit in collision:
			expl = Explosion(explosion_anim, superficie, hit.rect.center, 'alien')
			explosion.add(expl)
			sound = random.choice(explosion_sound)
			sound.play()

		for spe_ship in collision.values():
			stats.score = stats.score + ai_settings.special_ship_points * len(spe_ship)
			sb.prep_score()
		check_high_score(stats, sb)


def check_high_score(stats, sb):
	""""Verifica se há uma nova pontuação máxima."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
	return stats.high_score


def start_new_level(stats, sb):
	stats.level = stats.level + 1
	sb.prep_level()


def check_bullet_alien_collision(ai_settings, stats, sb, superficie, bullets, aliens,
								 espaconave, explosion, explosion_anim, explosion_sound, barreiras, alien):
	""""Responde a colisões entre projéteis e alienígenas."""
	# Remove qualquer projétil e alienígena que tenham colidido
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	if collisions:
		for hit in collisions:
			expl = Explosion(explosion_anim, superficie, hit.rect.center, 'alien')
			explosion.add(expl)
			sound = random.choice(explosion_sound)
			sound.play()

		for aliens in collisions.values():
			stats.score = stats.score + ai_settings.alien_points * len(aliens)
			sb.prep_score()
		check_high_score(stats, sb)


	if len(aliens) == 0:
		# Destrói os projéteis existentes e cria uma nova frota
		bullets.empty()
		ai_settings.increase_speed()

		# Timer bullet alien
		ai_settings.last_update = pygame.time.get_ticks()

		# Aumenta o nível
		start_new_level(stats, sb)

		if stats.level == 10:
			barreiras.empty()
			criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien)
		elif stats.level == 15:
			barreiras.empty()
			criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien)
		elif stats.level == 20:
			barreiras.empty()
			criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien)

		cria_frota(ai_settings, superficie, aliens, espaconave)

def obtem_numero_aliens(alien_largura, ai_settings):
	""""Determina o número de alienígenas que cabem em uma linha."""
	avaliando_space_x = ai_settings.superficie_largura - 2 * alien_largura
	numero_aliens_x = int(avaliando_space_x / (2 * alien_largura))
	return numero_aliens_x


def obetem_numero_linhas(ai_settings, alien_height, espaconave_height):
	""""Determina o número de linhas com alienígenas que cabem na tela."""
	avaliando_space_y = (ai_settings.superficie_altura -
						 	(10 * alien_height) - espaconave_height)
	numero_linhas = int(avaliando_space_y / (3.5 * alien_height))
	return numero_linhas


def cria_alien(ai_settings, superficie, alien_largura, aliens, numero_alien, numero_linha):
	""""Cria um alienígena e o posiciona na linha"""
	alien = Alien(ai_settings, superficie)
	alien.x = alien_largura + 2 * alien_largura * numero_alien
	alien.rect.x = alien.x
	alien.rect.y = (4 * alien.rect.height) + 2 * alien.rect.height * numero_linha
	aliens.add(alien)


def cria_frota(ai_settings, superficie, aliens, espaconave):
	""""Cria uma frota completa de alienígenas"""
	alien = Alien(ai_settings, superficie)
	alien_largura = alien.rect.width
	numero_aliens_x = obtem_numero_aliens(alien_largura, ai_settings)
	numero_linhas = obetem_numero_linhas(ai_settings, alien.rect.height,
										 	espaconave.rect.height)

	# Cria a primeira linha de alienígenas
	for numero_linha in range(numero_linhas):
		for numero_alien in range(numero_aliens_x):
			cria_alien(ai_settings, superficie, alien_largura, aliens, numero_alien, numero_linha)


def check_fleet_edges(ai_settings, superficie, aliens, bullet_aliens):
	""""Responde apropriadamente se algum alienígena alcançou uma borda."""
	for alien in aliens.sprites():
		if alien.check_edges():
			"""Faz toda a frota descer e muda a sua direção."""
			for alien in aliens.sprites():
				alien.rect.y = alien.rect.y + ai_settings.fleet_drop_speed
			ai_settings.fleet_direction = ai_settings.fleet_direction * -1
			break


def check_aliens_bottom(ai_settings, stats, sb, superficie, espaconave, aliens,
						bullets, bullet_aliens, music_game, explosion, explosion_anim,  play_button, special_ship, torpedo, barreiras):
	""""Verifica se algum alienígena alcançou a parte inferior da tela."""
	superficie_rect = superficie.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= superficie_rect.bottom:
			# Trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
			espaconave_hit(ai_settings, stats, sb, superficie,
						   espaconave, aliens, bullets, bullet_aliens,
						   music_game, explosion, explosion_anim,  play_button, special_ship, torpedo, barreiras)
			break


def update_aliens(ai_settings, stats, sb, superficie, espaconave, aliens, bullets, bullet_aliens,
				  music_game, explosion, explosion_anim, play_button, special_ship, torpedo, barreiras):
	""""Verifica se a frota está em uma das bordas
			e então atualiza as posições de todos os alienígenas da frota."""
	check_fleet_edges(ai_settings, superficie, aliens, bullet_aliens)
	aliens.update()

	# Verifica se houve colisões entre alienígenas e a espaçonave
	if pygame.sprite.spritecollideany(espaconave, aliens):
		espaconave_hit(ai_settings, stats, sb, superficie, espaconave, aliens,
					   bullets, bullet_aliens, music_game, explosion, explosion_anim,  play_button, special_ship, torpedo, barreiras)

	# Verifica se há algum alienígena que atingiu a parte inferior da tela
	check_aliens_bottom(ai_settings, stats, sb, superficie, espaconave,
						aliens, bullets, bullet_aliens, music_game, explosion, explosion_anim,  play_button, special_ship, torpedo, barreiras)

	check_aliens_collision_barreiras(barreiras, aliens)


def check_aliens_collision_barreiras(barreiras, aliens):
	collision = pygame.sprite.groupcollide(aliens, barreiras, False, False)
	if collision:
		barreiras.empty()


def espaconave_hit(ai_settings, stats, sb, superficie, espaconave, aliens,
				   bullets, bullet_aliens,  music_game, explosion, explosion_anim,  play_button, special_ship, torpedo, barreiras):
	""""Responde ao fato de a espaçonave ter sido atingida por um alienígena."""

	death_explosion = created_explosion_player(ai_settings, explosion_anim, superficie, espaconave, explosion)

	if death_explosion.alive():
		# Diminui a música
		pygame.mixer.music.set_volume(0)

	Cria_looping_de_imagem_explosao(ai_settings, superficie, espaconave, aliens, bullets, stats, sb, play_button,
									bullet_aliens, explosion, death_explosion, special_ship, torpedo, barreiras)

	if stats.espaconave_left > 0:
		diversos_fatores_aplicados_ship_hit(stats, sb, aliens, bullets, bullet_aliens, ai_settings, superficie,
											espaconave, special_ship, torpedo)
	else:
		stats.game_active = False
		# Inicia a música intro quando o jogo estiver na tela play
		music_game.music_intro()
		pygame.mouse.set_visible(True)


def armazena_na_list_imagens_explosoes():
	explosion_anim = {}
	explosion_anim['alien'] = []
	explosion_anim['ship'] = []
	explosion_anim['torpedo'] = []
	for i in range(9):
		# Criando diversas imagens de explosões e armazenando como valor (list) em um dicionário
		filename = 'images_explosion/regularExplosion0{}.png'.format(i)
		image_ex_alien = pygame.image.load(filename).convert()
		image_ex_alien.set_colorkey(0)
		img_transform_alien = pygame.transform.scale(image_ex_alien, (55, 45))
		explosion_anim['alien'].append(img_transform_alien)

		filename = 'player_explosion/sonicExplosion0{}.png'.format(i)
		image_ex_torpedo = pygame.image.load(filename).convert()
		image_ex_torpedo.set_colorkey(0)
		img_transform_alien = pygame.transform.scale(image_ex_alien, (165, 165))
		explosion_anim['torpedo'].append(img_transform_alien)

		filename = 'player_explosion/sonicExplosion0{}.png'.format(i)
		image_ex_ship = pygame.image.load(filename).convert()
		image_ex_ship.set_colorkey(0)
		explosion_anim['ship'].append(image_ex_ship)

	return explosion_anim


def direction_special_ship(ai_settings, sprite):
		if not sprite.alive() and not ai_settings.flag_creation_special_ship:
			ai_settings.direction_special_ship = ai_settings.direction_special_ship * -1
			ai_settings.flag_creation_special_ship = True


def remove_special_ship_edge(ai_settings, special_ship):
	for sprite in special_ship.sprites():
		if sprite.rect.right <= 0 or sprite.rect.left >= sprite.superficie_rect.right:
			special_ship.remove(sprite)
			direction_special_ship(ai_settings, sprite)


def created_camp_visao(sprite):
	tupla_cordenada_left = sprite.rect.bottomleft
	tupla_cordenada_right = sprite.rect.bottomright
	x_rect_left = tupla_cordenada_left[0]
	x_rect_right = tupla_cordenada_right[0]
	tupla = (x_rect_left, x_rect_right)
	return tupla


def created_torpedo(ai_settings, superficie, torpedo, sprite):
	if sprite.rect.right >= sprite.superficie_rect.right or sprite.rect.left <= sprite.superficie_rect.left:
		p_torpedo = Torpedo(ai_settings, superficie, sprite)
		torpedo.add(p_torpedo)


def created_special_ship(ai_settings, superficie, special_ship, sb, alien):
	now = pygame.time.get_ticks()
	if now - ai_settings.last_update_ship > ai_settings.time_aparecer_ms:

		if ai_settings.direction_special_ship == 1 and len(special_ship) == 0:
			ai_settings.last_update_ship = now + ai_settings.time_ship_draw
			especial_ship = Especial_ship(ai_settings, superficie, sb)
			special_ship.add(especial_ship)

			ai_settings.flag_creation_special_ship = False

		if ai_settings.direction_special_ship == -1 and len(special_ship) == 0:
			ai_settings.last_update_ship = now + ai_settings.time_ship_draw
			especial_ship = Especial_ship_left(ai_settings, superficie, sb)
			special_ship.add(especial_ship)

			ai_settings.flag_creation_special_ship = False


def update_torpedo(ai_settings, stats, sb, superficie, espaconave, aliens,
					   bullets, bullet_aliens, music_game, explosion, explosion_anim, play_button, special_ship,
					   torpedo, barreiras):
	for sprite in special_ship.sprites():
		if len(torpedo) == 0 and sprite.alive():
			created_torpedo(ai_settings, superficie, torpedo, sprite)

		for torp in torpedo.sprites():
			if sprite.alive():
				tupla_camp_visao = created_camp_visao(sprite)
				camp_v_left = tupla_camp_visao[0]
				camp_v_right = tupla_camp_visao[1]

				if (torp.rect.centerx >= camp_v_left and torp.rect.centerx <= camp_v_right) and (
					sprite.rect.left > sprite.superficie_rect.left and sprite.rect.right < sprite.superficie_rect.right):
					ai_settings.active = False

			if torp.rect.top >= torp.superficie_rect.bottom:
				torpedo.remove(torp)
				ai_settings.active = True

	torpedo.update()
	check_torpedo_collision_barreiras(ai_settings, barreiras, torpedo, explosion, explosion_anim, superficie)
	collision = pygame.sprite.spritecollide(espaconave, torpedo, True)
	if collision:
		espaconave_hit(ai_settings, stats, sb, superficie, espaconave, aliens,
					   bullets, bullet_aliens, music_game, explosion, explosion_anim, play_button, special_ship,
					   torpedo, barreiras)
	remove_special_ship_edge(ai_settings, special_ship)


def check_torpedo_collision_barreiras(ai_settings, barreiras, torpedo, explosion, explosion_anim, superficie):
	collission = pygame.sprite.groupcollide(torpedo, barreiras, True, True)
	if collission:
		for hit in collission:
			expl = Explosion(explosion_anim, superficie, hit.rect.center, 'torpedo')
			explosion.add(expl)
			sound = pygame.mixer.Sound("player_explosion/rumble1.ogg")
			sound.play()
		ai_settings.active = True


def update_special_ship(ai_settings, superficie, special_ship, sb, alien):
	created_special_ship(ai_settings, superficie, special_ship, sb, alien)
	special_ship.update()


def criando_barreiras(ai_settings, superficie, espaconave, barreiras, alien):
	square = Square(ai_settings, superficie, espaconave)
	avaliando_space_x = square.superficie_rect.width - 130 * square.rect.width
	square_number_x = int(avaliando_space_x / square.rect.width)

	avaliando_space_y = square.superficie_rect.height - espaconave.rect.height - (
		24.5 * alien.rect.height )
	number_linhas_y = int(avaliando_space_y / square.rect.height)


	for number_linha in range(number_linhas_y):
		for square_number in range(square_number_x):
			square = Square(ai_settings, superficie, espaconave)
			square.x = 16 * square.rect.width + square.rect.width * square_number
			square.rect.x = square.x

			square.y = 100 * square.rect.height + square.rect.height * number_linha
			square.rect.y = square.y
			barreiras.add(square)

	for number_linha in range(number_linhas_y):
		for square_number in range(square_number_x):
			square = Square(ai_settings, superficie, espaconave)
			square.x = 113 * square.rect.width + square.rect.width * square_number
			square.rect.x = square.x

			square.y = 100 * square.rect.height + square.rect.height * number_linha
			square.rect.y = square.y
			barreiras.add(square)

	for number_linha in range(number_linhas_y):
		for square_number in range(square_number_x):
			square = Square(ai_settings, superficie, espaconave)
			square.x = 64 * square.rect.width + square.rect.width * square_number
			square.rect.x = square.x

			square.y = 100 * square.rect.height + square.rect.height * number_linha
			square.rect.y = square.y
			barreiras.add(square)
















