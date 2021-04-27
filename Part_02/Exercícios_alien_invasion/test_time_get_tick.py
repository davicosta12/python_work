import pygame

def run_game():
	pygame.init()
	last_update = pygame.time.get_ticks()
	seconds = 10
	
	while True:
		now = pygame.time.get_ticks()
		if now - last_update > seconds:
			last_update = now
			print(last_update)


run_game()
