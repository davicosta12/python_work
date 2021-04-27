import pygame
from pygame.sprite import Sprite

class EspacoNave(Sprite):
	
	def __init__(self, ai_settings, superficie):
		"""Inicializa a espaçonave e define sua posição inicial."""
		super().__init__()
		self.superficie = superficie
		self.ai_settings = ai_settings
		
		# Carrega a imagem da espaçonave e obtém seu rect (retângulo)
		self.image = pygame.image.load('images/playerShip1_red.bmp')
		self.image.set_colorkey(0)


		self.rect = self.image.get_rect()
		self.superficie_rect = superficie.get_rect()
		
		#Inicia cada nova espaçonave na parte inferior central da tela
		self.rect.centerx = self.superficie_rect.centerx  # Eixo x 
		self.rect.bottom = self.superficie_rect.bottom   # Eixo y parte inferior
		
		# Armazena um valor decimal para o centro da espaçonave
		self.center = float(self.rect.centerx)
		
		# Flag de movimento
		self.moving_right = False
		self.moving_left = False

	
	def update(self):
		"""Atualiza a posição da espaçonave de acordo com a flag de movimento."""
		#Atualiza o valor do centro da espaçonave, e não o retângulo
		if self.moving_right and self.rect.right < self.superficie_rect.right:
			self.center = self.center + self.ai_settings.espaconave_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center = self.center - self.ai_settings.espaconave_speed_factor
		
		
		# Atualiza o objeto rect de acordo com self.center
		self.rect.centerx = self.center
	
	def blitme(self):
		"""Desenha a espaçonave em sua posição atual."""
		self.superficie.blit(self.image, self.rect)


	def center_espaconave(self):
		""""Centraliza a espaçonave na tela."""
		self.center = self.superficie_rect.centerx


