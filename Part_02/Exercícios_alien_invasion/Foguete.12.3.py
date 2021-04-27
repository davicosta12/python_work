import sys
import pygame

class Espaconave():
	# classe que foca só na espaço nave
	def __init__(self, configure, superficie):
		# montando a espaço nave
		self.configure = configure
		self.superficie = superficie

		self.imagem = pygame.image.load('imagem1.bmp')
		self.rect = self.imagem.get_rect()
		self.superficie_rect = self.superficie.get_rect()

		self.rect.centerx = self.superficie_rect.centerx
		self.rect.centery  = self.superficie_rect.centery

		self.center = float(self.rect.centerx)
		self.bottom = float(self.rect.bottom)

		# Flag de movimento
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False


	def update(self):
		# movimentação da espaçonave
		if self.moving_right and self.rect.right <  self.superficie_rect.right:
			self.center = self.center + self.configure.velocidade_da_ship
		if self.moving_left and self.rect.left > 0:
			self.center  = self.center  - self.configure.velocidade_da_ship
		if self.moving_up and self.rect.top > 0:
			self.bottom = self.bottom - self.configure.velocidade_da_ship
		if self.moving_down and self.rect.bottom < self.superficie_rect.bottom:
			self.bottom = self.bottom + self.configure.velocidade_da_ship

		self.rect.centerx = self.center
		self.rect.bottom = self.bottom


	def desenha_imagem_para_mim(self):
		# desenhando a imagem na tela
		self.superficie.blit(self.imagem, self.rect)


class Settings():
	# Configurações do jogo
	def __init__(self):
		# Configurações da tela
		self.superficie_largura = 1200
		self.superficie_altura = 800
		self.bg_color = (0, 150, 230)
		self.velocidade_da_ship = 1.5


def checa_eventos(espaconave):
	# Pega eventos do teclado e mouse
	for evento in pygame.event.get():
		if evento.type == pygame.QUIT:
			sys.exit()

		elif evento.type == pygame.KEYDOWN:
			if evento.key == pygame.K_RIGHT:
				espaconave.moving_right = True
			elif evento.key == pygame.K_LEFT:
				espaconave.moving_left = True
			elif evento.key == pygame.K_UP:
				espaconave.moving_up = True
			elif evento.key == pygame.K_DOWN:
				espaconave.moving_down = True

		elif evento.type == pygame.KEYUP:
			if evento.key == pygame.K_RIGHT:
				espaconave.moving_right = False
			elif evento.key == pygame.K_LEFT:
				espaconave.moving_left = False
			elif evento.key == pygame.K_UP:
				espaconave.moving_up = False
			elif evento.key == pygame.K_DOWN:
				espaconave.moving_down = False


def update_superficie(configure, superficie,  espaconave):
	# Redesenha a tela a cada loop
	superficie.fill(configure.bg_color)

	# Desenha a imagem
	espaconave.desenha_imagem_para_mim()

	# Pega a tela mais recente
	pygame.display.flip()

def run_game():
	pygame.init()

	configure = Settings()
	superficie = pygame.display.set_mode((configure.superficie_largura, configure.superficie_altura))
	pygame.display.set_caption("DOOM")

	# Criando uma espaço nave
	espaconave = Espaconave(configure, superficie)

	while True:
		checa_eventos(espaconave)
		espaconave.update()
		update_superficie(configure, superficie, espaconave)


run_game()
