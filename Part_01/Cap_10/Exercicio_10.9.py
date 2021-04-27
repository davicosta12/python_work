filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	try:
		with open(filename, "r") as file_reader:
			lista_animais = file_reader.readlines()
	
	except FileNotFoundError:
		pass         # Falha silenciosamente
	else:	
		for nome_animal in lista_animais:
			nome_animal = nome_animal.rstrip()
			print(nome_animal)
