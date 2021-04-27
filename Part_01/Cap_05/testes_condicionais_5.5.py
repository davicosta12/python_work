	# Cores de alienígenas #3

alien_color = input('Escolha a cor: ')

if alien_color == 'green' or alien_color.lower() == 'green':
	print('O jogador ganhou 5 pontos')
elif alien_color == 'yellow' or alien_color.lower() == 'yellow':
	print('O jogador ganhou 10 pontos')
elif alien_color == 'red' or alien_color.lower() == 'red':
	print('O jogador ganhou 15 pontos')
