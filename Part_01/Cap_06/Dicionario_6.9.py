favorite_places = {
	'davi': ['liberdade', 'morato', 'casa verde'],
	'andre': ['maripora', 'tijuca'],
	'rafaela': ['beco do batman', 'tiradentes'],		
	}

for nome, lugares in favorite_places.items():
	print("\n\n " + nome.title() + ":")
	for lugar in lugares:
		print("\t" + lugar.title())
