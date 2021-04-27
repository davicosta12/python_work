import sys
import pygame

def run_game():

	pygame.init()

	# Configurações
	superficie = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("DOOM")

	bg_color = (0, 180, 230)


	# Criando uma espaço nave
	imagem = pygame.image.load('imagem1.bmp')

	retangulo = imagem.get_rect()
	superficie_retangulo = 	superficie.get_rect()

	retangulo.centerx = superficie_retangulo.centerx
	retangulo.bottom = superficie_retangulo.bottom

	while True:
		# Pega eventos do teclado e mouse
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()


		# Redesenha a tela a cada loop
		superficie.fill(bg_color)

		# Desenha a imagem
		superficie.blit(imagem, retangulo)

		# Pega a tela mais recente
		pygame.display.flip()

run_game()
