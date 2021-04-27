# Percorrendo as chaves de um dicionário em ordem usando um laço

favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike'
}
# Crescente
for key in sorted(favorite_games.keys()):
	print(key)

print("\n\n")

# Decrescente	
for key in sorted(favorite_games.keys(), reverse = True):
	print(key)

# Printar somente os valores em um dicionário

print("\n\n")
print("Aqui estão os jogos")
for game in favorite_games.values():
	print(game.title())

print("\n\n")

favorite_games = {
	'davi': 'counter-strike',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike',
}
# O python printa os valores repetidos
for game in favorite_games.values():
	print(game.title())
print("\n\n")
# para nao printarmos os valores repetidos, podemos usar a função externa
# set()
for game in set(favorite_games.values()):
	print(game.title())
		
