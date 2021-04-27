# Se o nome das chaves forem iguais, o própio dicionário escolherá somente uma chave aleatoriamente,
# porém se tivermos chaves diferente, só que valores iguais, o python printará os dois.

# Exemplo 1 - valores repetidos e chaves não repetidas

favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike',
	'larissa': 'black',
	'rafaela': 'resident evil',
	'genilda': 'resident evil',
	'andre': 'black',		
}

for nome, jogo in favorite_games.items():
	print(nome)
	print(jogo + "\n")
	
print("\n\n")
	
# Exemplo 2 - valores não repetidos e chaves repetidas

favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike',
	'larissa': 'fifa',
	'marcos': 'resident evil',
	'davi': 'raibown six',
	'andre': 'black',		
}

for nome, jogo in favorite_games.items():
	print(nome)
	print(jogo + "\n")
	
print("\n\n")

# Exercício 
favorite_games = {
	'davi': 'call of duty',
	'marcos': 'minecraft',
	'vitor': 'roblox',
	'rafael': 'counter-strike',
	'larissa': 'fifa',
	'marcos': 'resident evil',
	'davi': 'raibown six',
	'andre': 'black',		
}

respondidos = ['davi', 'marcos']
	
for nome in favorite_games.keys():
	print("Reponda nossa enquete, " + nome.title())		
	if nome in respondidos:
		print("Obrigado por responder a enquete, " + 
			nome.title())
			
	
