import sys
import pygame

def run_game():
	
	pygame.init()
	
	superficie = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("DOOM")
	
	bg_color = (0, 180, 230)
	
	while True:
		# Pega eventos do teclado e mouse
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sys.exit()
		
		# Redesenha a tela a cada loop
		superficie.fill(bg_color)
		
		# Pega a tela mais recente
		pygame.display.flip()
		
run_game()

