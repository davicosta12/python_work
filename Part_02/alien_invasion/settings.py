import pygame
from os import path
from random import randint

class Settings():
	"""Uma classe para armazenar todas as configurações da Invasão Alienígena."""
	
	def __init__(self):
		"""Inicializa as confugurações do jogo."""

		#Configurações da tela
		back_ground_dir = path.join(path.dirname(__file__), 'images')
		self.back_ground_image = pygame.image.load(path.join(back_ground_dir, "backG.bmp"))
		self.back_ground_rect = self.back_ground_image.get_rect()
		self.superficie_largura = 1200
		self.superficie_altura = 950
		self.bg_color = (0, 0, 0)

		# configurações dos sons do jogo
		self.shoot_sound_alien = pygame.mixer.Sound("sounds/Laser_Shoot_alien.wav")
		self.shoot_sound = pygame.mixer.Sound("sounds/Laser_Shoot.wav")
		self.player_explosion = pygame.mixer.Sound("player_explosion/rumble1.ogg")

		#Configurações dos projéteis
		self.bullet_speed_factor = 2.5
		self.bullet_aliens_speed_factor = 2
		self.bullet_largura = 8
		self.bullet_altura = 30
		self.bullet_alien_color = 20, 150, 20
		self.bullet_color = 60, 60, 60
		self.bullets_permitidas = 3
		self.bullet_shoot_delay = 250
		self.bullet_last_shot = pygame.time.get_ticks()

		#Configurações dos alienígenas
		self.alien_speed_factor = 1.5
		self.fleet_drop_speed = 10
		#fleet_direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1

		#Configurações da espaçonave
		self.espaconave_speed_factor = 2
		self.espaconave_limit = 3

		#A taxa com que a velocidade do jogo aumenta ou diminui
		self.speedup_scale_special_ship = 1.05
		self.speeddown_scale_torp = 0.95
		self.speedup_scale = 1.1
		self.speeddown_scale = 0.9
		#A taxa com que os pontos para cada alienígena aumentam
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

		# Configurações da espacionave especial
		self.last_update_ship = pygame.time.get_ticks()
		self.especial_ship_speed_factor = 4
		self.direction_special_ship = 1
		self.flag_creation_special_ship = True
		self.time_aparecer_ms = 30000
		self.time_ship_draw = 4170

		# configurações do torpedo
		self.active = True
		self.torpedo_speed_factor = 1.8
		self.last_update_torpedo = pygame.time.get_ticks()

		#configurações do tempo de disparo dos projéteis alienígenas
		self.last_update = pygame.time.get_ticks()
		self.time_seconds = 5000


	def initialize_dynamic_settings(self):
		""""Inicializa as configurações que mudam no decorrer do jogo."""
		self.especial_ship_speed_factor = 1.2
		self.torpedo_speed_factor = 1.8
		self.espaconave_speed_factor = 2
		self.bullet_speed_factor = 2.5
		self.bullet_aliens_speed_factor = 2
		self.alien_speed_factor = 1.5
		self.time_seconds = 5000

		# fleet_direction igual a 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1

		# Pontuação
		self.alien_points = 50
		self.special_ship_points = 200

		# tempo

		# Configurações da espacionave especial
		self.last_update_ship = pygame.time.get_ticks()
		self.time_aparecer_ms = 30000
		self.time_ship_draw = 4170

		self.last_update_torpedo = pygame.time.get_ticks()

		# configurações do tempo de disparo dos projéteis alienígenas
		self.last_update = pygame.time.get_ticks()
		self.time_seconds = 5000

		self.active = True


	def increase_speed(self):
		""""Aumenta as configurações de velocidade."""
		Velocidade_special_ship_antes = self.especial_ship_speed_factor
		tempo_ap_special_ship_antes = self.time_ship_draw

		self.especial_ship_speed_factor = self.especial_ship_speed_factor  * self.speedup_scale_special_ship
		self.torpedo_speed_factor = self.torpedo_speed_factor * self.speedup_scale_special_ship
		self.time_aparecer_ms = self.time_aparecer_ms * self.speeddown_scale_torp
		self.time_ship_draw = (Velocidade_special_ship_antes / self.especial_ship_speed_factor) * (
			tempo_ap_special_ship_antes)

		self.espaconave_speed_factor = self.espaconave_speed_factor * self.speedup_scale
		self.bullet_speed_factor = self.bullet_speed_factor * self.speedup_scale
		self.bullet_aliens_speed_factor = self.bullet_aliens_speed_factor * self.speedup_scale
		self.alien_speed_factor = self.alien_speed_factor * self.speedup_scale
		self.time_seconds = self.time_seconds * self.speeddown_scale

		self.alien_points = int(self.alien_points * self.score_scale)
		self.special_ship_points = int(self.special_ship_points * self.score_scale)








