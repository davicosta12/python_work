robson = {
	'nome': 'robson',
	'tipo': 'tartaruga',
	'nome_dono': 'rafael',	 
	}

caca = {
	'nome': 'caca',
	'tipo': 'coelho',
	'nome_dono': 'adriana',
	}

tigre = {
	'nome': 'tigre',
	'tipo': 'cachorro',
	'nome_dono': 'andre',
	}
	
fred = {
	'nome': 'fred',
	'tipo': 'pato',
	'nome_dono': 'arthur',
	}

fifi = {
	'nome': 'fifi',
	'tipo': 'gato',
	'nome_dono': 'andre',
	}

dudu = {
	'nome': 'dudu',
	'tipo': 'hamster',
	'nome_dono': 'davi',
	}
	
pets = [robson, caca, tigre, fred, fifi, dudu]
for animal in pets:
	if animal == robson:
		print("\n\tO " + animal['nome'].title() + " é uma " +
			animal['tipo'] + " e seu dono se chama " +
			animal['nome_dono'].title() + ".")
	elif animal == caca:
		print("\n\tO " + animal['nome'].title() + " é um " +
			animal['tipo'] + " e sua dona se chama " +
			animal['nome_dono'].title() + ".")
	
	else:	
		print("\n\tO " + animal['nome'].title() + " é um " +
			animal['tipo'] + " e seu dono se chama " +
			animal['nome_dono'].title() + ".")
