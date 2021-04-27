# Grandes mágicos
def show_magicians(magicians_name):
	for nome in magicians_name:
		print(' \n ' + nome)
	
		
def make_great(magicians_name):
	i = 0
	for nome in magicians_name:
		magicians_name[i] = "o Grande " + nome
		i = i + 1
			
nomes_magicos = ['Mr. M', 'Dafo', 'Thelema', 'Artemis', 'Thelema']
make_great(nomes_magicos)
show_magicians(nomes_magicos)
