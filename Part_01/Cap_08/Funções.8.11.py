# Mágicos inalterados

def show_magicians(magicians_name):
	for nome in magicians_name:
		print(' \n ' + nome)
		
def make_great(magicians_name):
	i = 0
	for nome in magicians_name:
		magicians_name[i] = "o Grande " + nome
		i = i + 1
	return magicians_name
			
nomes_magicos = ['Mr. M', 'Dafo', 'Thelema', 'Artemis', 'Thelema']
Lista_modificada = make_great(nomes_magicos[:]) # ---> copia da lista original

show_magicians(nomes_magicos) # lista original inalterada
show_magicians(Lista_modificada) # copia foi modificada
