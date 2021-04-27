# Números favoritos - modificado

numeros_favoritos = {
	'rafael': [24, 22, 11, 3, 6, 0],
	'andre': [36, 2, 1, 9],
	'davi': [25, 1, 4, 3, 2, 1],
	'adriana': [26, 66, 76, 54, 11],
	'arthur': [51, 35],
}

for nome, numeros in numeros_favoritos.items():
	print("\n Os números favoritos do " + nome.title() + " é: \n")
	for numero in numeros:
		print(" " + str(numero))

