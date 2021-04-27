	# Cores de alienígenas #1

alien_color = input('Escolha a cor: ')

 # NÃO FALHA
if alien_color == 'green' or alien_color.lower() == 'green':
	print('O jogador acabou de ganhar 5 pontos.')

 # SEMPRE FALHA	
if alien_color == 1002 and alien_color.lower() == 'green': 
	print('O jogador acabou de ganhar 5 pontos.')
