# Lisa dentro do dicionário

# primeiro maneira

favorite_languages = {
	'davi': ['python', 'ruby'],
	'rafael': ['c'],
	'elias': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for nome, linguagens in favorite_languages.items():
	print("\n" + 'As linguagens favoritas do ' +
		nome.title() + ' é:')
	for linguagem in linguagens:
		print("\t" + linguagem.title())

print("\n\n")

# segunda maneira

favorite_languages = {
	'davi': ['python', 'ruby'],
	'rafael': ['c'],
	'elias': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
}

for nome, linguagens in favorite_languages.items():
	if len(linguagens) < 2:
		print("\nA linguagem favorita do " + nome.title() + " é:")
	else:
		print("\n" + "As linguagens favoritas do " +
			nome.title() + " é:")
	for linguagem in linguagens:
		print("\t" + linguagem.title())
		
