# Percorrendo o dicionário

favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike'
}
	# por padrão, os dicionários não se precupam com a ordem das chaves-valores printadas, quando usamos o for
	# a única coisa que o dicionárip se preocupa é a ordem que uma determinada chave aponta para seu valor
	# Percorrendo o dicionário sem ordem específica de chave-valor

# O método items() atribui tanto a chave, como o valor para as duas variáveis --> nome e jogo
for nome, jogo in favorite_games.items():
	print("\nO jogo favorito do " + nome.title() + " é: ")
	print(jogo.title())

# Podemos percorrer só a chaves, usando o método keys()
# obs: não é obrigatório usar o método keys(), pois a chave é por padrão associado como principal no dicionário
print("\n\n")
for key in favorite_games.keys():
	print(key)

print("\n\n")
if 'elisa' not in favorite_games:
	print("Elisa não está presente")
	
print("\n\n\n")	

	# Exemplo dicionário com lista

favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike'
}

amigos = ['marcos', 'rafael']
for nome in favorite_games.keys():
	print(nome.title())
	
	if nome in amigos:
		print(" Olá " + nome.title() +
			" eu conheço o seu jogo favorito que é " +
			favorite_games[nome].title())
