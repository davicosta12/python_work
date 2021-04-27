# Exemplos argumentos arbitrários
def make_sandwich(*tooping):  # o asterísco quer dizer que essa variável é arbitrátia, armazenando todos os argumentos passados, para essa função, em uma tupla.
	for ingrediente in tooping:
		print("\n - " + ingrediente)
